#!/usr/bin/env python
import os
import click
import codecs
import pandas as pd
import json
from collections import Counter

from nlppln.utils import create_dirs, out_file_name, get_files


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
@click.option('--name', '-n', default='freqs.csv')
@click.option('--mode', default='word')
def freqs(in_dir, out_dir, name, mode):
    if mode not in ('word', 'lemma'):
        raise ValueError("Unknown mode: {mode}, "
                         "please choose either word or lemma"
                         .format(**locals()))
    output_file = out_file_name(out_dir, name)
    create_dirs(output_file)

    in_files = get_files(in_dir)

    cnt = Counter()
    for fi in in_files:
        with codecs.open(fi, encoding='utf-8') as f:
            saf = json.load(f)
        for token in saf['tokens']:
            word = token[mode]
            pos = token['pos1']
            cnt.update({(word, pos): 1})
    data = [(word, pos, count) for ((word, pos), count) in cnt.most_common()]
    vocab_df = pd.DataFrame(data, columns=[mode, 'pos', 'cnt'])
    vocab_df['rank'] = vocab_df.index + 1
    vocab_df.to_csv(output_file, encoding='utf-8', index=False)


if __name__ == '__main__':
    freqs()
