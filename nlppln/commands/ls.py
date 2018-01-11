#!/usr/bin/env python
import click
import os
import json

from ..utils import cwl_file


@click.command()
@click.argument('dir_in', type=click.Path(exists=True))
@click.option('--recursive/--no-recursive', default=False)
@click.option('--endswith', default=None)
def command(dir_in, recursive, endswith):
    files_out = []

    if recursive:
        for root, dirs, files in os.walk(os.path.abspath(dir_in)):
            for f in files:
                files_out.append(cwl_file(os.path.join(root, f)))
    else:
        for f in os.listdir(dir_in):
            fi = os.path.join(dir_in, f)
            if os.path.isfile(fi):
                files_out.append(cwl_file(fi))

    # filter
    if endswith:
        files_out = filter(lambda x: x.get('path').endswith(endswith),
                           files_out)

    # order alphabetically on file name
    files_out = sorted(files_out, key=lambda x: x.get('path'))

    stdout_text = click.get_text_stream('stdout')
    stdout_text.write(json.dumps({'out_files': files_out}))


if __name__ == '__main__':
    command()
