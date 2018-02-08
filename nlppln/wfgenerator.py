from scriptcwl import WorkflowGenerator as WFGenerator

from .utils import CWL_PATH


class WorkflowGenerator(WFGenerator):
    def __init__(self, working_dir=None):
        WFGenerator.__init__(self, steps_dir=CWL_PATH, working_dir=working_dir)

        self.load(step_file='https://raw.githubusercontent.com/nlppln/'
                            'edlib-align/master/align.cwl')
        self.load(step_file='https://raw.githubusercontent.com/nlppln/'
                            'pattern-docker/master/pattern.cwl')

    def save(self, fname, validate=True, wd=False, inline=False, relative=True,
             pack=False, encoding='utf-8'):
        """Save workflow to file

        For nlppln, the default is to save workflows with relative paths.
        """
        super(WorkflowGenerator, self).save(fname,
                                            validate=validate,
                                            wd=wd,
                                            inline=inline,
                                            relative=relative,
                                            pack=pack,
                                            encoding=encoding)
