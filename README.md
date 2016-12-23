# NLP Pipeline

A python package to create NLP pipelines using [Common Workflow Language](http://www.commonwl.org/) (CWL).

Basically, it provides python scripts for common NLP tasks that can be run as
command line tools, and CWL specifications to use those tools. Most tools
wrap existing NLP functionality.
The command line tools are made with [Click](http://click.pocoo.org), a Python
package for creating command line interfaces.

## Installation

Install [Python](https://www.python.org/downloads/) 2.7.11 and
[pip](https://pip.pypa.io/en/stable/installing/).

We recommend installing `nlppln` in a
[virtual environment](https://virtualenv.pypa.io/en/stable/) (`pip install virtualenv`).

```
git clone https://github.com/WhatWorksWhenForWhom/nlppln.git
cd nlppln

virtualenv /path/to/env
source /path/to/env/bin/activate

git checkout develop
pip install cython
pip install -r requirements.txt
python setup.py develop
```

If you get an error while installing `nlppln`, it is most likely due to requirements
for xtas that are missing. Please have a look at the
[xtas installation instructions](http://xtas.net/setup.html#installation). We
are working on removing the dependency on xtas.

For the GUI:

Install [nodejs](https://nodejs.org/en/download/) (or via
[package manager](https://nodejs.org/en/download/package-manager/)) and
[npm](https://docs.npmjs.com/getting-started/installing-node)

Install [bower](https://bower.io/)
```
npm install -g bower
```

Then type:
```
npm install
bower install
```

Tools can be run by using the Python -m option, e.g. `python -m nlppln.guess_language <INPUTDIR> <OUTPUTFILE>`.

To run CWL workflows created with `nlppln`, install a cwl-runner (`pip install
cwlref-runner`) and [Docker](https://docs.docker.com/engine/installation/).

## Generating command line NLP tool boilerplate and cwl steps

NLP Pipeline contains functionality to generate command line NLP tools and CWL
steps. To generate a command line tool and/or CWL step run:

    python -m nlppln.generate

This command starts a command line interface that asks you to specify the inputs and outputs of the tool:

```
> python -m nlppln.generate
Generate python command? [y]:
Generate cwl step? [y]:
Command name [command]:
Metadata input file? [n]: y
Multiple input files? [y]:
Multiple output files? [y]:
Extension of output files? [json]:
Metadata output file? [n]: y
Save python command to [nlppln/command.py]:
Save metadata to? [metadata_out.csv]:
Save cwl step to [cwl/steps/command.cwl]:
```

## Workflows

### Anonymize

The anonmize-workflow finds named entities in all text files in a directory. Named entities
are replaced with their type (PER, LOC, ORG). The output consists of text files and a csv file that contains the named entities that have been replaced.

Usage:
```
cwl-runner /path/to/nlppln/cwl/anonymize.cwl --txt-dir /path/to/dir/with/text/files
```
The text files with named entities removed are saved in the directory where the pipeline is run.

## GUI

NLP Pipeline provides a GUI to inspect the results of running text processing workflows.
Currently, the GUI allows users to inspect the results of named entity recognition.

Command:

    python -m nlppln.inspect_ne <META IN> <IN FILES>

Results can be inspected at http://localhost:5000/ (the browser is started automatically).
For development, start the GUI with `python -m nlppln.gui.server <META IN> <IN FILES>`.
In this case, the GUI is started with `debug=True`.

Please note that the GUI requires some additional work (see [Installation](#installation)).
