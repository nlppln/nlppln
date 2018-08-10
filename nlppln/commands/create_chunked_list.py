#!/usr/bin/env python
import click
import codecs
import os
import json

from itertools import islice

from nlppln.utils import create_dirs, get_files


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.option('--size', '-s', default=500)
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
@click.option('--out_name', default='ls_chunk.json')
def create_chunked_list(in_dir, size, out_dir, out_name):
    """Create a division of the input files in chunks.

    The result is stored to a JSON file.
    """
    create_dirs(out_dir)

    in_files = get_files(in_dir)
    chunks = chunk(in_files, size)

    division = {}

    for i, files in enumerate(chunks):
        division[i] = [os.path.basename(f) for f in files]

    out_file = os.path.join(out_dir, out_name)
    with codecs.open(out_file, 'wb', encoding='utf-8') as f:
        json.dump(division, f, indent=4)


if __name__ == '__main__':
    create_chunked_list()
