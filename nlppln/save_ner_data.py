#!/usr/bin/env python
import click
import os
import codecs
import json
import pandas as pd


@click.command()
@click.argument('input_dir', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def nerstats(input_dir, output_file):
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frames = []

    files = os.listdir(input_dir)
    for fi in files:
        with codecs.open(os.path.join(input_dir, fi), encoding='utf-8') as f:
            saf = json.load(f)
        data = {}
        data['word'] = [t['word'] for t in saf['tokens'] if 'ne' in t.keys()]
        data['ner'] = [t['ne'] for t in saf['tokens'] if 'ne' in t.keys()]
        data['w_id'] = [t['id'] for t in saf['tokens'] if 'ne' in t.keys()]
        data['text'] = [fi for t in saf['tokens'] if 'ne' in t.keys()]

        frames.append(pd.DataFrame(data=data))

    df = pd.concat(frames, ignore_index=True)
    df.to_csv(output_file)


if __name__ == '__main__':
    nerstats()
