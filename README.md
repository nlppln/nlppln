# NLP Pipeline

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/24cd15fe1d9e4a51ab4be8c247e95c47)](https://www.codacy.com/app/jvdzwaan/nlppln?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=nlppln/nlppln&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/nlppln/nlppln.svg?branch=tests)](https://travis-ci.org/nlppln/nlppln)
[![Documentation Status](https://readthedocs.org/projects/nlppln/badge/?version=latest)](http://nlppln.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/nlppln.svg)](https://badge.fury.io/py/nlppln)
[![PyPI](https://img.shields.io/pypi/pyversions/nlppln.svg)](https://pypi.python.org/pypi/nlppln)
[![Documentation Status](http://readthedocs.org/projects/nlppln/badge/?version=latest)](http://nlppln.readthedocs.io/en/latest/?badge=latest)

A python package to create NLP pipelines using [Common Workflow Language](http://www.commonwl.org/) (CWL).

Basically, it provides python scripts for common NLP tasks that can be run as
command line tools, and CWL specifications to use those tools. Most tools
wrap existing NLP functionality.
The command line tools are made with [Click](http://click.pocoo.org), a Python
package for creating command line interfaces.

For creating new (e.g., project specific) NLP functionality, you can use [nlppln-gen](https://github.com/nlppln/nlppln-gen)
to generate boilerplate (i.e., empty) command line tools and CWL specifications.

## Installation

Install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git),
[Python](https://www.python.org/downloads/) 2.7 and [pip](https://pip.pypa.io/en/stable/installing/). (You also may need to install
  setuptools (`pip install setuptools`)).

We recommend installing `nlppln` in a
[virtual environment](https://virtualenv.pypa.io/en/stable/) (`pip install virtualenv`).

```
pip install nlppln
```

Tools can be run by using the Python -m option, e.g. `python -m nlppln.commands.apachetika <INPUTDIR> <OUTPUTDIR>`.

To run CWL workflows created with `nlppln`, install a cwl-runner:
```
pip install cwltool cwlref-runner`
```

Also install [Docker](https://docs.docker.com/engine/installation/) (required for use on Windows).

### For development

```
git clone https://github.com/nlppln/nlppln.git
cd nlppln

virtualenv /path/to/env
source /path/to/env/bin/activate

git checkout develop
pip install -r requirements.txt
python setup.py develop
```
## Creating workflows

Workflows can be created by writing a Python script.

```python
from nlppln import WorkflowGenerator

wf = WorkflowGenerator()
wf.load(steps_dir='/path/to/dir/with/cwl/steps/')

txt_dir = wf.add_inputs(txt_dir='Directory')

frogout = wf.frog_dir(dir_in=txt_dir)
saf = wf.frog_to_saf(in_files=frogout)
ner_stats = wf.save_ner_data(in_files=saf)
new_saf = wf.replace_ner(metadata=ner_stats, in_files=saf)
txt = wf.saf_to_txt(in_files=new_saf)

wf.add_outputs(ner_stats=ner_stats, txt=txt)

wf.save('anonymize.cwl')
```

Additional processing steps can be loaded using:

```python
from nlppln import WorkflowGenerator

wf = WorkflowGenerator()
wf.load(steps_dir='/path/to/dir/with/cwl/steps/')
```

To load a single cwl file, do:
```python
wf.load(step_file='/path/to/step_or_workflow.cwl')
```

See [scriptcwl](https://github.com/NLeSC/scriptcwl) for more information on creating
workflows.

## Workflows

### Anonymize

The anonmize-workflow finds named entities in all text files in a directory. Named entities
are replaced with their type (PER, LOC, ORG). The output consists of text files and a csv file that contains the named entities that have been replaced.

Usage:
```
cwl-runner /path/to/nlppln/cwl/anonymize.cwl --txt-dir /path/to/dir/with/text/files
```
The text files with named entities removed are saved in the directory where the pipeline is run.
