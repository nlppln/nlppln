#!/usr/bin/env python
import click
import codecs
import json
import os
import pyjq
import pandas as pd

from nlppln.utils import create_dirs


@click.command()
@click.argument('in_files', nargs=-1, type=click.Path(exists=True))
@click.argument('meta_out', nargs=1, type=click.Path())
def command(in_files, meta_out):
    create_dirs(meta_out)

    d = {'num_words': [], 'num_sentences': []}

    text_names = []

    for fi in in_files:
        with codecs.open(fi, encoding='utf-8') as f:
            text = json.load(f, encoding='utf-8')

        text_id = os.path.splitext(os.path.basename(fi))[0]
        text_names.append(text_id)
        d['num_words'].append(len(text['tokens']))
        num_sentences = len(pyjq.one('[.tokens[].sentence] | unique', text))
        d['num_sentences'].append(num_sentences)

    df = pd.DataFrame(d, index=text_names)
    df.to_csv(meta_out, encoding='utf-8')


if __name__ == '__main__':
    command()
