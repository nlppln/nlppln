# NLP Pipeline

A python package to create NLP pipelines using [Common Workflow Language](http://www.commonwl.org/) (CWL).

Basically, it provides python scripts that wrap existing NLP functionality, mostly
through [xtas](http://xtas.net/), and CWL specifications to use those scripts.

## Installation

```
git clone https://github.com/WhatWorksWhenForWhom/nlpppln.git
cd nlpppln
git checkout develop
python setup.py develop
```

Scripts can be run by using the Python -m option, e.g. `python -m nlpppln.guess_language <INPUTDIR> <OUTPUTFILE>`.
