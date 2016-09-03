#!/usr/bin/env python
import pandas as pd
from codecs import open


def load_ner_csv(csv, nan_replacement='NE'):
    with open(csv, encoding='utf-8') as f:
        df = pd.read_csv(f, index_col=0)

    return df.fillna(nan_replacement)
