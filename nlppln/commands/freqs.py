#!/usr/bin/env python
import click
import codecs
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd

def make_corpus(doc_files):
    for doc in doc_files:
        with codecs.open(doc, encoding='utf-8') as f:
            yield f.read()

@click.command()
@click.argument('in_files', nargs=-1, type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def freqs(in_files, output_file):
    vectorizer = CountVectorizer(min_df=1)
    corpus = make_corpus(in_files)
    X = vectorizer.fit_transform(corpus)
    freqs = np.array(X.sum(axis=0)).squeeze()
    vocab_df = pd.DataFrame(
        {'word': vectorizer.get_feature_names(), 'freq': freqs})
    vocab_df['rank'] = vocab_df['freq'].rank(method='first', ascending=False)
    vocab_df = vocab_df.sort('rank')
    vocab_df.to_csv(output_file, encoding='utf-8', index=False)



if __name__ == '__main__':
    freqs()
