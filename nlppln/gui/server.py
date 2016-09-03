import pandas as pd
from codecs import open

from flask import Flask, render_template
from flask.json import jsonify
from flask_bootstrap import Bootstrap
from flask_bower import Bower
from flask_triangle import Triangle


app = Flask(__name__)
Bootstrap(app)
Bower(app)
Triangle(app)
app.config['meta_in'] = '/home/jvdzwaan/data/tmp/ner-statistics.csv'


@app.route('/')
def index():
    """Returns the HTML of the angular app (single page application)

    This is done in Flask (and not angular), because we want to be able to
    start the webserver from Python.
    """
    return render_template('named_entities.html')


@app.route('/named_entities')
def named_entities():
    meta_in = app.config.get('meta_in')

    with open(meta_in, encoding='utf-8') as f:
        df = pd.read_csv(f, index_col=0)

    df = df.fillna('NE')

    return jsonify(data=df.to_dict(orient='records'))


@app.route('/texts')
def texts():
    meta_in = app.config.get('meta_in')

    with open(meta_in, encoding='utf-8') as f:
        df = pd.read_csv(f, index_col=0)

    print list(set(df['text']))

    return jsonify(data=list(set(df['text'])))


if __name__ == '__main__':
    app.run(debug=True)
