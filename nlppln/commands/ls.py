#!/usr/bin/env python
import click
import json

from ..utils import get_files, cwl_file


@click.command()
@click.argument('dir_in', type=click.Path(exists=True))
@click.option('--recursive/--no-recursive', default=False)
@click.option('--endswith', default=None)
def command(dir_in, recursive, endswith):
    files_out = []

    files_out = get_files(dir_in, recursive=recursive)

    # filter
    if endswith:
        files_out = filter(lambda x: x.endswith(endswith), files_out)

    files_out = [cwl_file(f) for f in files_out]

    stdout_text = click.get_text_stream('stdout')
    stdout_text.write(json.dumps({'out_files': files_out}))


if __name__ == '__main__':
    command()
