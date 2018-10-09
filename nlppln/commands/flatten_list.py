#!/usr/bin/env python
import click
import json
import codecs
import itertools


@click.command()
def command():
    with codecs.open('files.json', encoding='utf-8') as data:
        list_of_lists = json.load(data)

    flattened = list(itertools.chain(*list_of_lists))

    stdout_text = click.get_text_stream('stdout')
    stdout_text.write(json.dumps({'out_files': flattened}))


if __name__ == '__main__':
    command()
