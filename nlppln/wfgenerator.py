from scriptcwl import WorkflowGenerator as WFGenerator

from .utils import CWL_PATH


class WorkflowGenerator(WFGenerator):
    def __init__(self):
        WFGenerator.__init__(self, steps_dir=CWL_PATH)

    def save(self, fname, inline=True, relative=False, validate=True,
             encoding='utf-8'):
        """Save workflow to file

        For nlppln, the default is to save steps inline.
        """
        super(WorkflowGenerator, self).save(fname,
                                            inline=inline,
                                            relative=relative,
                                            validate=validate,
                                            encoding=encoding)
