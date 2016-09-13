#!/usr/bin/env python
import click
import os
import codecs
import json


@click.command()
@click.argument('param_name')
@click.argument('input_dir', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def command(param_name, input_dir, output_file):
    """Generate a json file that specifies an input file list for a cwl step.
    """
    output_dir = os.path.dirname(os.path.abspath(output_file))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    json_out = {}
    json_out[param_name] = []

    files = os.listdir(input_dir)
    for fi in files:
        full_name = os.path.join(input_dir, fi)
        json_out[param_name].append({'class': 'File', 'path': full_name})

    with codecs.open(output_file, 'wb', encoding='utf-8') as f:
        json.dump(json_out, f, indent=4)

if __name__ == '__main__':
    command()
