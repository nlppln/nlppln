from scriptcwl import WorkflowGenerator as WFGenerator

from .utils import CWL_PATH


class WorkflowGenerator(WFGenerator):
    def __init__(self, working_dir=None):
        WFGenerator.__init__(self, steps_dir=CWL_PATH, working_dir=working_dir)

    def save(self, fname, validate=True, wd=True, inline=False, relative=False,
             pack=False, encoding='utf-8'):
        """Save workflow to file

        For nlppln, the default is to use a working directory (and save steps
        using the ``wd`` option).
        """
        super(WorkflowGenerator, self).save(fname,
                                            validate=validate,
                                            wd=wd,
                                            inline=inline,
                                            relative=relative,
                                            pack=pack,
                                            encoding=encoding)
