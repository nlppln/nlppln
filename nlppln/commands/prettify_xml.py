#!/usr/bin/env python
import click
import codecs
import os

from bs4 import BeautifulSoup

from nlppln.utils import create_dirs, out_file_name


@click.command()
@click.argument('in_file', type=click.File(encoding='utf-8'))
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
def prettify_xml(in_file, out_dir):
    create_dirs(out_dir)

    bs = BeautifulSoup(in_file.read(), 'xml')

    out_file = out_file_name(out_dir, in_file.name, 'xml')
    with codecs.open(out_file, 'wb', encoding='utf-8') as f:
        f.write(bs.prettify())


if __name__ == '__main__':
    prettify_xml()
