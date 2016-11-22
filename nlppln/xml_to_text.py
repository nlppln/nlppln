#!/usr/bin/env python
import click
import codecs
from lxml import etree

from nlppln.utils import create_dirs, out_file_name


@click.command()
@click.argument('in_files', nargs=-1, type=click.Path(exists=True))
@click.argument('out_dir', nargs=1, type=click.Path())
@click.option('--tag', default=None)
def command(in_files, out_dir, tag):
    create_dirs(out_dir)

    for fi in in_files:
        with codecs.open(fi, encoding='utf-8') as f:
            root = etree.ElementTree().parse(f)
        if tag is not None:
            elements = list(root.iter('{*}' + tag))
        else:
            elements = [root]
        texts = []
        for el in elements:
            texts.append(' '.join(
            [e.text for e in el.iterdescendants() if
             e.text is not None]))

        out_file = out_file_name(out_dir, fi, 'txt')
        with codecs.open(out_file, 'wb', encoding='utf-8') as f:
            f.write('\n'.join(texts))
            f.write('\n')


if __name__ == '__main__':
    command()
