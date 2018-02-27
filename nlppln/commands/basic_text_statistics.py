#!/usr/bin/env python
import click
import codecs
import json
import os
import pandas as pd

from nlppln.utils import create_dirs, get_files


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.argument('meta_out', type=click.Path())
def basic_text_statistics(in_dir, meta_out):
    create_dirs(meta_out)

    d = {'num_words': [], 'num_sentences': []}

    text_names = []

    in_files = get_files(in_dir)

    for fi in in_files:
        with codecs.open(fi, encoding='utf-8') as f:
            text = json.load(f, encoding='utf-8')

        text_id = os.path.splitext(os.path.basename(fi))[0]
        text_names.append(text_id)
        d['num_words'].append(len(text['tokens']))
        sentences = [t['sentence'] for t in text['tokens']]
        num_sentences = len(set(sentences))
        d['num_sentences'].append(num_sentences)

    df = pd.DataFrame(d, index=text_names)
    df.to_csv(meta_out, encoding='utf-8')


if __name__ == '__main__':
    basic_text_statistics()
