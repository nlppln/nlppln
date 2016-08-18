#!/usr/bin/env python
import click
import os
import codecs

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('nlppln', 'templates'),
                  trim_blocks=True)


def to_bool(v):
    """Convert 'y' to True and 'n' to False or raise an error."""
    if v == 'y':
        return True
    elif v == 'n':
        return False
    raise ValueError('Invalid input "{}" (only "y" or "n" are allowed)'.
                     format(v))


@click.command()
@click.option('--cname', prompt='Command name', default='command')
@click.option('--meta_in', prompt='Metadata input file?', default='n')
@click.option('--inputs', prompt='Multiple input files?', default='y')
@click.option('--outputs', prompt='Multiple output files?', default='y')
def command(cname, meta_in, inputs, outputs):
    """Generate a cwl file that specifies an nlppln processing step.
    """
    meta_in = to_bool(meta_in)
    inputs = to_bool(inputs)
    outputs = to_bool(outputs)

    ob = None
    if outputs:
        ob = click.prompt('Output binding', default='*.json')

    meta_out = click.prompt('Metadata output file?', default='n')
    meta_out = to_bool(meta_out)

    if meta_out:
        meta_out_file = click.prompt('Save metadata to?', type=click.Path(),
                                     default='metadata_out.csv')
        if meta_out_file.startswith('/'):
            meta_out_file = meta_out_file[1:]

    template = env.get_template('step.cwl')

    r = template.render(command_name=cname, output_binding=ob, meta_in=meta_in,
                        inputs=inputs, outputs=outputs, meta_out=meta_out)

    default = './cwl/steps/{}.cwl'.format(cname.replace('_', '-'))
    out_file = click.prompt('Save command to', type=click.Path(),
                            default=default)

    output_dir = os.path.dirname(out_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with codecs.open(out_file, 'wb', encoding='utf-8') as f:
        f.write(r)
        f.write('\n')


if __name__ == '__main__':
    command()
