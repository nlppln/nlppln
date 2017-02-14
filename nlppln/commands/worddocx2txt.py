#!/usr/bin/env python
import click
import codecs
import docx2txt

from nlppln.utils import create_dirs, out_file_name


@click.command()
@click.argument('in_files', nargs=-1, type=click.Path(exists=True))
@click.argument('out_dir', nargs=1, type=click.Path())
def command(in_files, out_dir):
    create_dirs(out_dir)

    for fi in in_files:
        try:
            text = docx2txt.process(fi)

            out_file = out_file_name(out_dir, fi, 'txt')
            with codecs.open(out_file, 'wb', encoding='utf-8') as f:
                f.write(text)
                f.write('\n')
        except Exception as e:
            click.echo('Error in file: {}'.format(fi))
            click.echo(e)

if __name__ == '__main__':
    command()
