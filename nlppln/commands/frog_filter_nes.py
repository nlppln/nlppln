#!/usr/bin/env python
import click
import os

import pandas as pd

from nlppln.utils import create_dirs


@click.command()
@click.argument('ner_statistics', type=click.Path(exists=True))
@click.option('--keep', '-k', multiple=True, default=[u'PER', u'LOC'])
@click.option('--name', default='ner_statistics.csv')
@click.option('--out_dir', u'-o', default=os.getcwd(), type=click.Path())
def command(ner_statistics, keep, name, out_dir):
    df = pd.read_csv(ner_statistics, index_col=0, encoding='utf-8')

    df = df.query(u' or '.join([u'ner=="{}"'.format(k) for k in keep]))

    output_file = os.path.join(out_dir, name)
    create_dirs(output_file)
    df.to_csv(output_file, encoding='utf-8')

if __name__ == '__main__':
    command()
