#!/usr/bin/env python
import click
import os
import shutil
import uuid

from nlppln.utils import create_dirs, out_file_name


@click.command()
@click.argument('in_file', type=click.Path(exists=True))
@click.option('--rename', type=click.Choice(['random', 'spaces', 'copy']),
              default='spaces')
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
def command(in_file, rename, out_dir):
    create_dirs(out_dir)

    ext = os.path.splitext(in_file)[1].replace('.', '')
    fname = os.path.basename(in_file)

    if rename == 'spaces':
        fname = fname.replace(' ', '-')
    elif rename == 'random':
        fname = '{}.{}'.format(uuid.uuid4(), ext)

    fo = out_file_name(out_dir, fname)
    shutil.copy2(in_file, fo)

if __name__ == '__main__':
    command()
