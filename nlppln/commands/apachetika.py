#!/usr/bin/env python
import click
import codecs
import tika
from tika import parser

from nlppln.utils import create_dirs, out_file_name


@click.command()
@click.argument('in_files', nargs=-1, type=click.Path(exists=True))
@click.argument('out_dir', nargs=1, type=click.Path())
@click.option('--tika_server', nargs=1)
def command(in_files, out_dir, tika_server):
    create_dirs(out_dir)

    for fi in in_files:
        if tika_server:
            parsed = parser.from_file(fi, tika_server)
        else:
            parsed = parser.from_file(fi)

        out_file = out_file_name(out_dir, fi, 'txt')
        with codecs.open(out_file, 'wb', encoding='utf-8') as f:
            f.write(parsed['content'])


if __name__ == '__main__':
    command()
