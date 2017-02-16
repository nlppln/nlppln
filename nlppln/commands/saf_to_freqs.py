#!/usr/bin/env python
import click
import codecs
import os
import pandas as pd
import json
from collections import Counter


@click.command()
@click.argument('in_files', nargs=-1, type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--mode', default='word')
def freqs(in_files, output_file, mode):
    if mode not in ('word', 'lemma'):
        raise ValueError("Unknown mode: {mode}, "
                         "please choose either word or lemma"
                         .format(**locals()))

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
