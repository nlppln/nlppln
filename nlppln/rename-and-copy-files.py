#!/usr/bin/env python
import click
import os
import shutil

from nlppln.utils import create_dirs


@click.command()
@click.argument('in_files', nargs=-1, type=click.Path(exists=True))
@click.argument('out_dir', nargs=1, type=click.Path())
def command(in_files, out_dir):
    create_dirs(out_dir)

    for fi in in_files:
        fo = fi.replace(' ', '-')
        fo = os.path.basename(fo)
        fo = os.path.join(out_dir, fo)
        shutil.copy2(fi, fo)

if __name__ == '__main__':
    command()
