#!/usr/bin/env python
import click
import os
import codecs
import json
import pandas as pd


@click.command()
@click.argument('input_files', nargs=-1, type=click.Path(exists=True))
@click.argument('output_file', nargs=1, type=click.Path())
def nerstats(input_files, output_file):
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frames = []

    for fi in input_files:
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
    df.to_csv(output_file)


if __name__ == '__main__':
    nerstats()
