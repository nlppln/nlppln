#!/usr/bin/env python
import click
import codecs
import os
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer

from ..utils import create_dirs, get_files, split


def load_liwc_dict(dict_file, encoding):

    with codecs.open(dict_file, 'rb', encoding) as f:
        lines = f.readlines()

    liwc_categories = {}
    liwc_dict = {}

    for line in lines:
        # LIWC category
        if line[0].isdigit():
            entry = line.split()
            # remove 0 from strings like 01
            c = str(int(entry[0]))
            liwc_categories[c] = entry[1]
        # word
        elif line[0].isalpha():
            entry = line.split()
            term = entry[0]
            categories = entry[1:]
            liwc_dict[term] = categories
    return liwc_dict, liwc_categories


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.argument('liwc_dict', type=click.Path(exists=True))
@click.option('--encoding', '-e', default='latin1',
              help='Encoding of LIWC dictionary.')
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
@click.option('--name', '-n', default='liwc.csv')
def command(in_dir, liwc_dict, encoding, out_dir, name):
    create_dirs(out_dir)

    in_files = get_files(in_dir)

    liwc, liwc_categories = load_liwc_dict(liwc_dict, encoding)

    text_ids = [os.path.basename(fi) for fi in in_files]
    cols = liwc_categories.values()
    result = pd.DataFrame(0, index=text_ids, columns=cols)

    # make vocabulary
    count_vect = CountVectorizer(input='filename', tokenizer=split)
    word_counts = count_vect.fit_transform(in_files)

    # get total number of words per text
    result['#words'] = word_counts.sum(axis=1)

    # get words that match the liwc regexes (these should be added to the
    # vocabluary)
    liwc_regexes = [w for w in liwc.keys() if '*' in w]
    for w in liwc_regexes:
        # remove last character (*) from liwc entry
        start = w[0:len(w)-1]
        for word in count_vect.vocabulary_:
            if word.startswith(start):
                liwc[word] = liwc[w]
        del liwc[w]

    # get frequencies for all liwc words
    count_vect = CountVectorizer(input='filename', vocabulary=liwc.keys())
    word_counts = count_vect.fit_transform(in_files)

    # sum over categories
    # http://stackoverflow.com/questions/37013115/how-to-read-traverse-slice-scipy-sparse-matrices-lil-csr-coo-dok-faster
    word_counts_csc = word_counts.tocsc()
    for word, categories in liwc.iteritems():
        w_idx = count_vect.vocabulary_.get(word)
        col = np.zeros(len(in_files))
        A = word_counts_csc.getcol(w_idx)
        for i, d in zip(A.indices, A.data):
            col[i] = d

        for cat in categories:
            result[liwc_categories[cat]] += col

    lc = liwc_categories.values()
    result[lc] = result[lc].div(result['#words'], axis='index')
    result[lc] = result[lc]*100.0

    out_file = os.path.join(out_dir, name)
    result.to_csv(out_file, encoding='utf-8')


if __name__ == '__main__':
    command()
