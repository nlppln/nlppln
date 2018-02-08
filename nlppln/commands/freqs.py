#!/usr/bin/env python
import os
import click
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd

from nlppln.utils import create_dirs, get_files, split


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
@click.option('--name', '-n', default='freqs.csv')
def freqs(in_dir, out_dir, name):
    out_file = os.path.join(out_dir, name)
    create_dirs(out_file)

    in_files = get_files(in_dir)

    vectorizer = CountVectorizer(input='filename', tokenizer=split)
    X = vectorizer.fit_transform(in_files)
    freqs = np.array(X.sum(axis=0)).squeeze()
    vocab_df = pd.DataFrame(
        {'word': vectorizer.get_feature_names(), 'freq': freqs})
    vocab_df['rank'] = vocab_df['freq'].rank(method='first', ascending=False)
    vocab_df = vocab_df.sort('rank')
    vocab_df.to_csv(out_file, encoding='utf-8', index=False)


if __name__ == '__main__':
    freqs()
