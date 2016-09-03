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
    df = load_ner_csv(app.config.get('meta_in'))

    return jsonify(data=df.to_dict(orient='records'))


@app.route('/texts')
def texts():
    df = load_ner_csv(app.config.get('meta_in'))

    return jsonify(data=list(set(df['text'])))


if __name__ == '__main__':
    app.run(debug=True)
