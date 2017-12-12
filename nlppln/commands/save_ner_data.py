#!/usr/bin/env python
import click
import os
import codecs
import json
import pandas as pd

from nlppln.utils import create_dirs, get_files


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
@click.option('--name', '-n', default='ner_stats.csv')
def nerstats(in_dir, out_dir, name):
    create_dirs(out_dir)

    frames = []

    in_files = get_files(in_dir)

    for fi in in_files:
        with codecs.open(fi, encoding='utf-8') as f:
            saf = json.load(f)
        data = {}
        data['word'] = [t['word'] for t in saf['tokens'] if 'ne' in t.keys()]
        data['ner'] = [t['ne'] for t in saf['tokens'] if 'ne' in t.keys()]
        data['w_id'] = [t['id'] for t in saf['tokens'] if 'ne' in t.keys()]
        data['text'] = [os.path.basename(fi)
                        for t in saf['tokens'] if 'ne' in t.keys()]

        frames.append(pd.DataFrame(data=data))

    df = pd.concat(frames, ignore_index=True)
    df.to_csv(os.path.join(out_dir, name), encoding='utf-8')


if __name__ == '__main__':
    nerstats()
