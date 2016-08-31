import pandas as pd
from codecs import open

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_bower import Bower


app = Flask(__name__)
Bootstrap(app)
Bower(app)
app.config['meta_in'] = '/home/jvdzwaan/data/tmp/ner-statistics.csv'


@app.route('/named_entities')
def named_entities_overview():
    meta_in = app.config.get('meta_in')
    with open(meta_in, encoding='utf-8') as f:
        df = pd.read_csv(f, index_col=0)

    df = df.fillna('NE')
    gr = df.groupby('text')

    print gr.groups.keys()
    for group in gr.groups.keys():
        print gr.get_group(group)
    return render_template('named_entities.html', texts=gr.groups.keys(),
                           num_named_entities=len(df),
                           data=df.to_json(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
