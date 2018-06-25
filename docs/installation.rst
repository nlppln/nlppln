Installation
============

Requirements
############

Before installing nlppln, please install:

* `Python 2 or 3 <https://www.python.org/downloads/>`_
* `node.js <https://nodejs.org/en/download/>`_
* `Docker <https://docs.docker.com/engine/installation/>`_

For more details about CWL on Windows, see the `Windows documentation <https://github.com/common-workflow-language/cwltool/blob/master/windowsdoc.md>`_.

Installing nlppln
#################

Install nlppln using pip:

.. code-block:: sh

  pip install nlppln

For development:

.. code-block:: sh

  git clone git@github.com:nlppln/nlppln.git
  cd nlppln
  pip install -r requirements.txt
  python setup.py develop

Run tests (including coverage) with:

.. code-block:: sh

  python setup.py develop test
