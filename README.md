# NLP Pipeline

A python package to create NLP pipelines using [Common Workflow Language](http://www.commonwl.org/) (CWL).

Basically, it provides python scripts for common NLP tasks that can be run as
command line tools, and CWL specifications to use those tools. Most tools
wrap existing NLP functionality, usually through [xtas](http://xtas.net/).
The command line tools are made with [Click](http://click.pocoo.org), a Python
package for creating command line interfaces.

## Installation

```
git clone https://github.com/WhatWorksWhenForWhom/nlppln.git
cd nlppln
git checkout develop
python setup.py develop
```

For the GUI:

```
npm install
bower install
```

Tools can be run by using the Python -m option, e.g. `python -m nlppln.guess_language <INPUTDIR> <OUTPUTFILE>`.

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
are replaced with their type (PER, LOC, ORG). The output consists of saf-files.

Usage:
```
> cwl-runner /path/to/nlppln/cwl/workflows/anonymize.cwl --txt-dir <IN FILES>
```

## GUI

NLP Pipeline provides a GUI to inspect the results of running text processing workflows.
Currently, the GUI allows users to inspect the results of named entity recognition.

Command:

    python -m nlppln.inspect_ne <META IN> <IN FILES>

Results can be inspected at http://localhost:5000/ (the browser is started automatically).
For development, start the GUI with `python -m nlppln.gui.server <META IN> <IN FILES>`.
In this case, the GUI is started with `debug=True`.

Please note that the GUI requires some additional work (see [Installation](#installation)).
