#!/usr/bin/env python
import click
import codecs
import os
import re

from string import punctuation

from nlppln.utils import create_dirs, out_file_name


def normalize_whitespace(text):
    return u' '.join(text.split())


def normalize_punctuation(text):
    for c in punctuation:
        try:
            if c == u'.':
                text = re.sub(r'\{}+'.format(c), c, text)
            else:
                text = re.sub(r'{}+'.format(c), c, text)
        except:
            if c != u'\\':
                text = re.sub(r'\{}+'.format(c), c, text)
    return text


@click.command()
@click.argument('txt', type=click.File(encoding='utf-8'))
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
def normalize_whitespace_punctuation(txt, out_dir):
    create_dirs(out_dir)

    text = txt.read()
    text = normalize_whitespace(text)
    text = normalize_punctuation(text)

    out_file = out_file_name(out_dir, os.path.basename(txt.name))
    with codecs.open(out_file, 'wb', encoding='utf-8') as f:
        f.write(text)


if __name__ == '__main__':
    normalize_whitespace_punctuation()
