#!/usr/bin/env python
import click
import threading
import webbrowser

from gui.server import app


@click.command()
@click.argument('meta_in', type=click.Path(exists=True))
#@click.argument('in_files', nargs=-1, type=click.Path(exists=True))
def command(meta_in):
    #df = pd.read_csv(meta_in, index_col=0)
    #df = df.fillna('NE')
    #print df

    url = 'localhost:5000/inspect'

    threading.Timer(1.25, lambda: webbrowser.open(url, new=2)).start()
    #raise NoAppException('test')

    #for fi in in_files:
    #    with codecs.open(fi, encoding='utf-8') as f:
    #        pass

    app.config['meta_in'] = meta_in
    app.run()



if __name__ == '__main__':
    command()
