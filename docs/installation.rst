Installation
============

Install nlppln using pip:

.. code-block:: sh

  pip install nlppln

For development:

.. code-block:: sh

  git clone git@github.com:nlppln/nlppln.git
  cd nlppln
  git checkout develop
  pip install -r requirements.txt
  python setup.py develop

Run tests (including coverage) with:

.. code-block:: sh

  python setup.py develop test

Docker
######

Some nlppln text processing steps are run in Docker containers. Therefore, we recommend
that you install `Docker <https://docs.docker.com/engine/installation/>`_.
Docker takes away the hassle of having to install nlp tools. Instead they are run
in a container.

Windows
#######

On Windows, all processing steps and workflows are executed in Docker Containers, so
`installing Docker <https://docs.docker.com/docker-for-windows/>`_ is a requirement
for using nlppln.

To install cwltool on Windows, you need

* `Python 2 or 3 <https://www.python.org/downloads/windows/>`_
* `Docker <https://docs.docker.com/docker-for-windows/>`_
* `node.js <https://nodejs.org/en/download/>`_

After installing the requirements, install nlppln
::

  pip install nlppln

For more details about CWL on Windows, see the `Windows documentation <https://github.com/common-workflow-language/cwltool/blob/master/windowsdoc.md>`_.
