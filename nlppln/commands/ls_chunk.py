#!/usr/bin/env python
import click
import os
import json

from nlppln.utils import cwl_file


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.argument('chunks', type=click.File(encoding='utf-8'))
@click.argument('name')
def ls_chunk(in_dir, chunks, name):
    div = json.load(chunks)
    files = div.get(name, [])
    files_out = [cwl_file(os.path.abspath(os.path.join(in_dir, f)))
                 for f in files]

    stdout_text = click.get_text_stream('stdout')
    stdout_text.write(json.dumps({'out_files': files_out}))

if __name__ == '__main__':
    ls_chunk()
