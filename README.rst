NLP Pipeline
============

|codacy_grade| |travis| |documentation| |pypi_version| |pypi_supported| |zenodo|

nlppln is a python package for creating NLP pipelines using `Common Workflow Language <http://www.commonwl.org/>`_ (CWL).
It provides steps for (generic) NLP functionality, such as tokenization,
lemmatization, and part of speech tagging, and helps users to construct workflows
from these steps.

A text processing step consist of a (Python) command line tool and a CWL
specification to use this tool.
Most tools provided by nppln wrap existing NLP functionality.
The command line tools are made with `Click <http://click.pocoo.org>`_, a Python
package for creating command line interfaces.

To create a workflow, you have to write a Python script:
::

  from nlppln import WorkflowGenerator

  with WorkflowGenerator() as wf:
    txt_dir = wf.add_input(txt_dir='Directory')

    frogout = wf.frog_dir(in_dir=txt_dir)
    saf = wf.frog_to_saf(in_files=frogout)
    ner_stats = wf.save_ner_data(in_files=saf)
    new_saf = wf.replace_ner(metadata=ner_stats, in_files=saf)
    txt = wf.saf_to_txt(in_files=new_saf)

    wf.add_outputs(ner_stats=ner_stats, txt=txt)

    wf.save('anonymize.cwl')

The resulting workflow can be run using a CWL runner, such as `cwltool <https://github.com/common-workflow-language/cwltool/>`_:

.. code-block:: sh

  cwltool anonymize.cwl --txt_dir /path/to/directory/with/txt/files/

For creating new (e.g., project specific) NLP functionality, you can use `nlppln-gen <https://github.com/nlppln/nlppln-gen>`_
to generate boilerplate (i.e., empty) command line tools and CWL specifications.

The full documentation can be found on `Read the Docs <http://nlppln.readthedocs.io/en/latest/>`_.

Installation
############

Install nlppln using pip:

.. code-block:: sh

  pip install nlppln

Please check the `installation guidelines <http://nlppln.readthedocs.io/en/latest/installation.html>`_ for additional required software.

License
#######

Copyright (c) 2016-2018, Netherlands eScience Center, University of Twente

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

.. |codacy_grade| image:: https://api.codacy.com/project/badge/Grade/24cd15fe1d9e4a51ab4be8c247e95c47
                     :target: https://www.codacy.com/app/jvdzwaan/nlppln?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=nlppln/nlppln&amp;utm_campaign=Badge_Grade
                     :alt: Codacy Badge

.. |travis| image:: https://travis-ci.org/nlppln/nlppln.svg?branch=master
              :target: https://travis-ci.org/nlppln/nlppln
              :alt: Build Status

.. |documentation| image:: https://readthedocs.org/projects/nlppln/badge/?version=latest
                     :target: http://nlppln.readthedocs.io/en/latest/?badge=latest
                     :alt: Documentation Status

.. |pypi_version| image:: https://badge.fury.io/py/nlppln.svg
                    :target: https://badge.fury.io/py/nlppln
                    :alt: PyPI version

.. |pypi_supported| image:: https://img.shields.io/pypi/pyversions/nlppln.svg
                      :target: https://pypi.python.org/pypi/nlppln
                      :alt: PyPI

.. |zenodo| image:: https://zenodo.org/badge/65198876.svg
              :target: https://zenodo.org/badge/latestdoi/65198876
              :alt: DOI
