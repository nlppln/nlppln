#!/usr/bin/env python
import click
import codecs
import os
import json
import datetime
import pattern
from pattern.nl import parsetree

from nlppln.utils import create_dirs, out_file_name


def parse(text):
    tokens = []
    p = parsetree(text,
                  tokenize=True,     # Split punctuation marks from words?
                  tags=True,         # Parse part-of-speech tags? (NN, JJ, ...)
                  chunks=False,      # Parse chunks? (NP, VP, PNP, ...)
                  relations=False,   # Parse chunk relations? (-SBJ, -OBJ, ...)
                  lemmata=True,      # Parse lemmata? (ate => eat)
                  encoding='utf-8',  # Input string encoding.
                  tagset=None)       # Penn Treebank II (default) or UNIVERSAL.
    for sentence_id, sentence in enumerate(p):
        for word_id, word in enumerate(sentence):
            tokens.append({'id': word_id,
                           'word': word.string,
                           'lemma': word.lemma,
                           'sentence': sentence_id,
                           'pos': word.type})
    return tokens


@click.command()
@click.argument('in_files', nargs=-1, type=click.Path(exists=True))
@click.option('--out_dir', '-o', default=os.getcwd(), nargs=1, type=click.Path())
def command(in_files, out_dir):
    create_dirs(out_dir)

    for fi in in_files:
        with codecs.open(fi, encoding='utf-8') as f:
            text = f.read()
        tokens = parse(text)

        pattern_version = pattern.__version__
        header = {
                    'format': 'SAF',
                    'format-version': '0.1',
                    'processed': [{
                        'module': "pattern.nl",
                        'module-version': pattern_version,
                        'started': datetime.date.today().strftime('%Y-%m-%d')
                    }]
                }

        out_file = out_file_name(out_dir, fi, 'json')
        with codecs.open(out_file, 'wb', encoding='utf-8') as f:
            json.dump({'header': header, 'tokens': tokens}, f, indent=4)


if __name__ == '__main__':
    command()
