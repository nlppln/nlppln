#!/usr/bin/env python
import click
import urllib

from nlppln.utils import create_dirs


@click.command()
@click.argument('urls', nargs=-1, type=click.STRING)
@click.argument('out_dir', nargs=1, type=click.Path())
def command(urls, out_dir):
    create_dirs(out_dir)

    for url in urls:
        try:
            fname = url.split('/')[-1]
            urllib.urlretrieve(url, fname)
        except Exception as e:
            click.echo(str(e))


if __name__ == '__main__':
    command()
