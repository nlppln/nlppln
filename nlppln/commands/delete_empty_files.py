#!/usr/bin/env python
import click
import codecs
import os
import shutil
from nlppln.utils import create_dirs, out_file_name, get_files


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
def delete_empty_files(in_dir, out_dir):
    create_dirs(out_dir)

    in_files = get_files(in_dir)
    for fi in in_files:
        with codecs.open(fi, encoding='utf-8') as f:
            text = f.read()

        if len(text.strip()) > 0:
            fname = out_file_name(out_dir, fi)
            try:
                shutil.copy2(fi, fname)
            except shutil.Error:
                pass
        else:
            print('deleting {}'.format(os.path.basename(fi)))
            if os.path.abspath(in_dir) == os.path.abspath(out_dir):
                os.remove(fi)


if __name__ == '__main__':
    delete_empty_files()
