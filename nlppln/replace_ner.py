#!/usr/bin/env python
import click
import os
import codecs
import json
import pandas as pd


@click.command()
@click.argument('ner_csv_file', type=click.Path(exists=True))
@click.argument('input_files', nargs=-1, type=click.Path(exists=True))
@click.argument('output_dir', nargs=1, type=click.Path())
@click.option('--mode', default='replace')
def command(ner_csv_file, input_files, output_dir, mode):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if mode not in ('replace', 'delete'):
        raise ValueError("Unknown mode: {mode}, "
                         "please choose either replace or delete"
                         .format(**locals()))

    ners = pd.read_csv(ner_csv_file, index_col=0, encoding='utf-8')
    ners = ners.fillna('NE')
    grouped = ners.groupby(['text'])

    for fi in input_files:
        with codecs.open(fi, encoding='utf-8') as f:
            saf = json.load(f)

        bn = os.path.basename(fi)
        df = grouped.get_group(bn).set_index('w_id')
        ner_data = df.to_dict()

        for t in saf['tokens']:
            if t['id'] in ner_data['text'].keys():
                if mode == 'replace':
                    r = ner_data['ner'][t['id']]
                    t['word'] = r
                    t['lemma'] = r
                elif mode == 'delete':
                    t['word'] = ''
                    t['lemma'] = ''

        out_file = os.path.join(output_dir, bn)
        with codecs.open(out_file, 'wb', encoding='utf-8') as f:
            json.dump(saf, f, indent=4)


if __name__ == '__main__':
    command()
