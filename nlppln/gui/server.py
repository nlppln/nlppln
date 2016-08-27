import pandas as pd
from codecs import open

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.config['meta_in'] = '/Users/janneke/Downloads/cwl/ner-statistics.csv'


@app.route('/named_entities')
def named_entities_overview():
    meta_in = app.config.get('meta_in')
    with open(meta_in, encoding='utf-8') as f:
        df = pd.read_csv(f, index_col=0)

    df = df.fillna('NE')
    df = df.groupby('text')

    print df.groups.keys()
    for group in df.groups.keys():
        print df.get_group(group)
    return render_template('named_entities.html', texts=df.groups.keys())


if __name__ == '__main__':
    app.run(debug=True)
