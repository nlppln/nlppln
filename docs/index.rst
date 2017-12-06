.. nlppln documentation master file, created by
   sphinx-quickstart on Tue Nov 28 16:27:45 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the nlppln documentation!
====================================

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
    txt_dir = wf.add_inputs(txt_dir='Directory')

    frogout = wf.frog_dir(dir_in=txt_dir)
    saf = wf.frog_to_saf(in_files=frogout)
    ner_stats = wf.save_ner_data(in_files=saf)
    new_saf = wf.replace_ner(metadata=ner_stats, in_files=saf)
    txt = wf.saf_to_txt(in_files=new_saf)

    wf.add_outputs(ner_stats=ner_stats, txt=txt)

    wf.save('anonymize.cwl')

The resulting workflow can be run using a CWL runner, such as `cwltool <https://github.com/common-workflow-language/cwltool/>`_:

.. code-block:: none

  cwltool anonymize.cwl --txt_dir /path/to/directory/with/txt/files/

For creating new (e.g., project specific) NLP functionality, you can use `nlppln-gen <https://github.com/nlppln/nlppln-gen>`_
to generate boilerplate (i.e., empty) command line tools and CWL specifications.

Flexible and reproducible text processing workflows
###################################################

One of the problems with existing NLP software is that to combine functionality
from different software packages, researchers have to write custom scripts.
Generally, these scripts duplicate at least some text processing tasks (e.g.,
tokenization), and need to be adapted when used for new datasets or in other software
or hardware environments. This has a negative impact on research reproducibility and
reuse of existing software.

The main advantages of nlppln are:

* Flexibility: it is easy to combine NLP tools written in different programming languages
* Reproducibility and portability: the resulting workflows can be run on a wide variety of hardware environments without changing them

Contents
########
.. toctree::
   :maxdepth: 2

   installation
   creating_workflows
   running_workflows
   tools
