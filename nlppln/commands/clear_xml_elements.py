#!/usr/bin/env python
import click
import codecs
import os
from bs4 import BeautifulSoup
from nlppln.utils import create_dirs, out_file_name


@click.command()
@click.argument('xml_file', type=click.File())
@click.option('--element', '-e', multiple=True)
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
def command(xml_file, element, out_dir):
    create_dirs(out_dir)

    bs = BeautifulSoup(xml_file.read(), 'xml')

    for elem in element:
        to_empty = bs.find_all(elem)
        for t in to_empty:
            t.clear()

    out_file = out_file_name(out_dir, os.path.basename(xml_file.name))
    with codecs.open(out_file, 'wb', encoding='utf-8') as f:
        f.write(bs.prettify())

if __name__ == '__main__':
    command()
