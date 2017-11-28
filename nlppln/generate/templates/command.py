#!/usr/bin/env python
import click
import codecs
{% if outputs or meta_out %}import os{% endif %}

{% if outputs or meta_out or inputs %}
from nlppln.utils import {% if outputs or meta_out %}create_dirs, out_file_name{% endif %}{% if inputs and (outputs or meta_out) %}, {% endif %}{% if inputs %}get_files{% endif %}
{% endif %}



@click.command()
{% if meta_in %}
@click.argument('meta_in', type=click.File(encoding='utf-8'))
{% endif %}
{% if inputs %}
@click.argument('in_dir', type=click.Path(exists=True))
{% endif %}
{% if meta_out %}
@click.option('--name', '-n', default='{{meta_out_file}}')
{% endif %}
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
def {{command_name}}({{args}}):
{% if outputs or meta_out %}
    create_dirs(out_dir)
{% endif %}

{% if inputs %}
    in_files = get_files(in_dir)
    for fi in in_files:
        with codecs.open(fi, encoding='utf-8') as f:
            pass

{% if outputs %}
        out_file = out_file_name(out_dir, fi, '{{extension}}')
        with codecs.open(out_file, 'wb', encoding='utf-8') as f:
            pass

{% endif %}
{% endif %}
{% if meta_out %}
    out_file = out_file_name(out_dir, name)
    with codecs.open(out_file, 'wb', encoding='utf-8') as f:
        pass

{% endif %}

if __name__ == '__main__':
    {{command_name}}()
