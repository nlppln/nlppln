#!/usr/bin/env python
import click
import os
import codecs
import pandas as pd

from xtas.tasks.single import guess_language


@click.command()
@click.argument('input_dir', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def guess(input_dir, output_file):
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = {}
    data['language'] = []

    txt_files = os.listdir(input_dir)
    for txt_file in txt_files:
        with codecs.open(os.path.join(input_dir, txt_file)) as f:
            txt = f.read()
        data['language'].append(guess_language(txt)[0])

    df = pd.DataFrame(data=data, index=txt_files)
    df.to_csv(output_file)

if __name__ == '__main__':
    guess()
