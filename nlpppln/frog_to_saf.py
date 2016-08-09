#!/usr/bin/env python
import click
import os
import codecs
import json

from xtas.tasks._frog import parse_frog, frog_to_saf


@click.command()
@click.argument('input_dir', type=click.Path(exists=True))
@click.argument('output_dir', type=click.Path())
def frog2saf(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frog_files = os.listdir(input_dir)
    for fi in frog_files:
        with codecs.open(os.path.join(input_dir, fi)) as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
        saf_data = frog_to_saf(parse_frog(lines))

        out_file = os.path.join(output_dir, '{}.json'.format(fi))
        with codecs.open(out_file, 'wb', encoding='utf-8') as f:
            json.dump(saf_data, f, indent=4)


if __name__ == '__main__':
    frog2saf()
