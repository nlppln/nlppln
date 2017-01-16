#!/usr/bin/env python
import click
import threading
import webbrowser
import os

from gui.server import app


@click.command()
@click.argument('meta_in', type=click.Path(exists=True))
@click.argument('in_files', nargs=-1, type=click.Path(exists=True))
def command(meta_in, in_files):
    url = 'http://localhost:5000'

    threading.Timer(1.25, lambda: webbrowser.open(url, new=2)).start()

    app.config['meta_in'] = meta_in
    app.config['dir_in'] = os.path.dirname(in_files[0])
    app.run()


if __name__ == '__main__':
    command()
