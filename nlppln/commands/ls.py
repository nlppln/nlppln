#!/usr/bin/env python
import click
import os
import json


@click.command()
@click.argument('dir_in', type=click.Path(exists=True))
def command(dir_in):
    files_out = []

    for root, dirs, files in os.walk(os.path.abspath(dir_in)):
        for f in files:
            fi = {'class': 'File', 'path': os.path.join(root, f)}
            files_out.append(fi)

    stdout_text = click.get_text_stream('stdout')
    stdout_text.write(json.dumps({'files': files_out}))


if __name__ == '__main__':
    command()
