import pandas as pd
import numpy as np
from codecs import open
import json
import os

from flask import Flask, render_template
from flask.json import jsonify
from flask_bootstrap import Bootstrap
from flask_bower import Bower
from flask_triangle import Triangle

from utils import load_ner_csv

app = Flask(__name__)
Bootstrap(app)
Bower(app)
Triangle(app)


@app.route('/')
def index():
    """Returns the HTML of the angular app (single page application)

    This is done in Flask (and not angular), because we want to be able to
    start the webserver from Python.
    """
    return render_template('named_entities.html')


@app.route('/named_entities')
def named_entities():
    df = load_ner_csv(app.config.get('meta_in'))

    return jsonify(data=df.to_dict(orient='records'))


@app.route('/named_entities_aggr')
def named_entities_aggr():
    df = load_ner_csv(app.config.get('meta_in'))

    grouped = df.groupby(['ner', 'word'])
    r = grouped.count()
    r['text_count'] = grouped['text'].apply(lambda x: len(set(x)))
    r['word'] = r.index.get_level_values('word')
    r['ner'] = r.index.get_level_values('ner')

    r.columns = ['count' if c == 'w_id' else c for c in r.columns]
    r = r.drop('text', 1)

    return jsonify(data=r.to_dict(orient='records'))


@app.route('/texts')
def texts():
    df = load_ner_csv(app.config.get('meta_in'))

    return jsonify(data=list(set(df['text'])))


@app.route('/overview_named_entities')
def overview_named_entities():
    df = load_ner_csv(app.config.get('meta_in'))

    grouped = df.groupby(['text', 'ner'])
    df = grouped.count()
    df = df.drop('w_id', 1)
    df.columns = ['count']

    texts = list(set([text for text, _ in df.index]))
    result = pd.concat([df.loc[t] for t in texts], axis=1)
    result = result.fillna(0)
    r = result.T
    r['text'] = texts
    columns = ['NE', 'ORG', 'LOC', 'PER']
    r[columns] = r[columns].astype(int)
    num_ne = np.sum(r[columns].values)
    r['total'] = r.sum(axis=1)
    return jsonify(data=r.to_dict(orient='records'), texts=texts, nes=num_ne)


@app.route('/text/<text>')
def get_text(text):
    text = os.path.join(app.config.get('dir_in'), text)
    with open(text, encoding='utf-8') as f:
        saf = json.load(f)

    return jsonify(data=saf.get('tokens'))


@app.route('/named_entities_text/<text>')
def named_entities_text(text):
    df = load_ner_csv(app.config.get('meta_in'))
    # filter data
    df = df[df['text'] == text]
    grouped = df.groupby(['word', 'ner'])
    df = grouped.count()
    df['word'] = df.index.get_level_values('word')
    df['ner'] = df.index.get_level_values('ner')

    return jsonify(data=df.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
