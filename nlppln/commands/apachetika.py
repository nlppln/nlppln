#!/usr/bin/env python
import click
import codecs
import os
import tika
from tika import parser

from nlppln.utils import create_dirs, out_file_name, get_files


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
@click.option('--tika_server')
def command(in_dir, out_dir, tika_server):
    create_dirs(out_dir)

    in_files = get_files(in_dir)

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
