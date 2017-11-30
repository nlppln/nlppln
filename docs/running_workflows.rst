Running workflows
=================

To run a workflow created with nlppln, you need to use a CWL runner. The default
CWL runner cwltool is installed when you install nlppln. To run a tool:
::

	cwltool <workflow> <inputs>

The scriptcwl documentation contains some `tips and tricks for working with CWL files <http://scriptcwl.readthedocs.io/en/latest/cwl_tips_tricks.html>`_.

Windows
#######

To run a workflow created with nlppln on Windows, use the nlppln Docker container:
::

  cwltool --default-container nlppln:nlppln <workflow> <inputs>

Also, if you have to refer to file paths with spaces in them, use the
``--relax-path-checks`` option.

For more details about CWL on Windows, see the `Windows documentation <https://github.com/common-workflow-language/cwltool/blob/master/windowsdoc.md>`_.
