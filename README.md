# NLP Pipeline

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/24cd15fe1d9e4a51ab4be8c247e95c47)](https://www.codacy.com/app/jvdzwaan/nlppln?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=nlppln/nlppln&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/nlppln/nlppln.svg?branch=master)](https://travis-ci.org/nlppln/nlppln)
[![Documentation Status](https://readthedocs.org/projects/nlppln/badge/?version=latest)](http://nlppln.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/nlppln.svg)](https://badge.fury.io/py/nlppln)
[![PyPI](https://img.shields.io/pypi/pyversions/nlppln.svg)](https://pypi.python.org/pypi/nlppln)

nlppln is a python package for creating NLP pipelines using [Common Workflow Language](http://www.commonwl.org/) (CWL).
It provides steps for (generic) NLP functionality, such as tokenization,
lemmatization, and part of speech tagging, and helps users to construct workflows
from these steps.

A text processing step consist of a (Python) command line tool and a CWL
specification to use this tool.
Most tools provided by nppln wrap existing NLP functionality.
The command line tools are made with [Click](http://click.pocoo.org), a Python
package for creating command line interfaces.

To create a workflow, you have to write a Python script:

```python
from nlppln import WorkflowGenerator

with WorkflowGenerator() as wf:
  txt_dir = wf.add_inputs(txt_dir='Directory')

  frogout = wf.frog_dir(dir_in=txt_dir)
  saf = wf.frog_to_saf(in_files=frogout)
  ner_stats = wf.save_ner_data(in_files=saf)
  new_saf = wf.replace_ner(metadata=ner_stats, in_files=saf)
  txt = wf.saf_to_txt(in_files=new_saf)

  wf.add_outputs(ner_stats=ner_stats, txt=txt)

  wf.save('anonymize.cwl')
```

The resulting workflow can be run using a CWL runner, such as [cwltool](https://github.com/common-workflow-language/cwltool/):

```
cwltool anonymize.cwl --txt_dir /path/to/directory/with/txt/files/
```

For creating new (e.g., project specific) NLP functionality, you can use [nlppln-gen](https://github.com/nlppln/nlppln-gen>)
to generate boilerplate (i.e., empty) command line tools and CWL specifications.

More detailed information can be found in the [documentation](http://nlppln.readthedocs.io/en/latest/).

## Installation

Install nlppln using pip:

```
pip install nlppln
```
