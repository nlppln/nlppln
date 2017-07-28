#!/usr/bin/env python
import click
import codecs
{% if outputs %}import os{% endif %}

{% if outputs or meta_out %}
from nlppln.utils import create_dirs{% if outputs %}, out_file_name{% endif %}
{% endif %}



@click.command()
{% if meta_in %}
@click.argument('meta_in', type=click.Path(exists=True))
{% endif %}
{% if inputs %}
@click.argument('in_files', nargs=-1, type=click.Path(exists=True))
{% endif %}
{% if outputs %}
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
{% endif %}
{% if meta_out %}
@click.argument('meta_out', nargs=1, type=click.Path())
{% endif %}
def {{command_name}}({{args}}):
{% if outputs %}
    create_dirs(out_dir)
{% endif %}
{% if meta_out %}
    create_dirs(meta_out)
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

    with codecs.open(meta_out, 'wb', encoding='utf-8') as f:
        pass
{% endif %}


if __name__ == '__main__':
    {{command_name}}()
