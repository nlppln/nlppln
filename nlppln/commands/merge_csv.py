#!/usr/bin/env python
import click
import codecs
import os

from nlppln.utils import create_dirs, out_file_name, get_files


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
@click.option('--name', '-n', default='merged.csv')
def merge_csv(in_dir, out_dir, name):
    create_dirs(out_dir)

    in_files = get_files(in_dir)

    wrote_header = False

    out_file = out_file_name(out_dir, name)
    with codecs.open(out_file, 'wb', encoding='utf-8') as fo:
        for fi in in_files:
            with codecs.open(fi, encoding='utf-8') as f:
                lines = f.readlines()
            if len(lines) > 1:
                header = lines[0]
                data = lines[1:]

                # TODO: check if headers are the same
                if not wrote_header:
                    fo.write(header)
                    wrote_header = True
                for line in data:
                    fo.write(line)

if __name__ == '__main__':
    merge_csv()
