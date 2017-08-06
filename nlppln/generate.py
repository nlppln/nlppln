#!/usr/bin/env python
import click
import sys
import codecs

from collections import OrderedDict
from jinja2 import Environment, PackageLoader

from .utils import create_dirs

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
def command():
    """Generate a cwl file that specifies an nlppln processing step.
    """
    script = click.prompt('Generate python command?', default='y',
                          type=click.Choice(['y', 'n']))
    script = to_bool(script)

    step = click.prompt('Generate cwl step?', default='y',
                        type=click.Choice(['y', 'n']))
    step = to_bool(step)

    if not script and not step:
        click.echo('Not generating script and not generating cwl step.')
        sys.exit()

    cname = click.prompt('Command name', default='command')

    meta_in = click.prompt('Metadata input file?', default='n',
                           type=click.Choice(['y', 'n']))
    meta_in = to_bool(meta_in)

    inputs = click.prompt('Multiple input files?', default='y',
                          type=click.Choice(['y', 'n']))
    inputs = to_bool(inputs)

    outputs = click.prompt('Multiple output files?', default='y',
                           type=click.Choice(['y', 'n']))
    outputs = to_bool(outputs)

    ext = None
    glb = None
    if outputs and step:
        glb = click.prompt('Glob pattern of output files?', default='*.json')
        ext = glb.split('.')[-1]

    meta_out = click.prompt('Metadata output file?', default='n',
                            type=click.Choice(['y', 'n']))
    meta_out = to_bool(meta_out)

    meta_out_file = None
    if meta_out:
        meta_out_file = click.prompt('Save metadata to?',
                                     type=click.Path(),
                                     default='metadata_out.csv')
        if meta_out_file.startswith('/'):
            meta_out_file = meta_out_file[1:]

    if script:
        d = OrderedDict({'meta_in': meta_in,
                         'in_dir': inputs,
                         'name': meta_out})
        args = [a for a in d.keys() if d[a]]
        args.append('out_dir')

        template = env.get_template('command.py')
        r = template.render(command_name=cname, extension=ext, meta_in=meta_in,
                            inputs=inputs, outputs=outputs, meta_out=meta_out,
                            args=', '.join(args), meta_out_file=meta_out_file)

        default = 'nlppln/commands/{}.py'.format(cname)
        out_file = click.prompt('Save python command to', type=click.Path(),
                                default=default)
        create_dirs(out_file)
        with codecs.open(out_file, 'wb', encoding='utf-8') as f:
            f.write(r)

    if step:
        template = env.get_template('step.cwl')

        r = template.render(command_name=cname, glob=glb, meta_in=meta_in,
                            inputs=inputs, outputs=outputs, meta_out=meta_out,
                            meta_out_file=meta_out_file)

        default = 'cwl/{}.cwl'.format(cname.replace('_', '-'))
        out_file = click.prompt('Save cwl step to', type=click.Path(),
                                default=default)

        create_dirs(out_file)
        with codecs.open(out_file, 'wb', encoding='utf-8') as f:
            f.write(r)
            f.write('\n')


if __name__ == '__main__':
    command()
