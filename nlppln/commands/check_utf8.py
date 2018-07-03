#!/usr/bin/env python
import click
import os
import codecs
import shutil

from bs4 import UnicodeDammit
from functools import partial
from multiprocessing import Pool

from nlppln.utils import create_dirs, get_files, out_file_name


def check_file(in_file, convert, out_dir):
    fo = out_file_name(out_dir, in_file)
    try:
        with codecs.open(in_file, encoding='utf-8') as f:
            text = f.read()
        if convert:
            # don't copy if it's the same file
            if os.path.abspath(in_file) != fo:
                shutil.copy2(in_file, fo)
    except UnicodeDecodeError:
        with codecs.open(in_file, 'rb') as f:
            text = f.read()
        dammit = UnicodeDammit(text)
        print('{}: {}'.format(in_file, dammit.original_encoding))
        if convert:
            with codecs.open(fo, 'w', encoding='utf-8') as f:
                f.write(dammit.unicode_markup)


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.option('--convert/--no-convert', default=False)
@click.option('--processes', '-p', default=1)
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
def check_utf8(in_dir, convert, processes, out_dir):
    create_dirs(out_dir)
    in_files = get_files(in_dir)

    check = partial(check_file, convert=convert, out_dir=out_dir)

    pool = Pool(processes=processes)
    pool.map(check, in_files)


if __name__ == '__main__':
    check_utf8()
