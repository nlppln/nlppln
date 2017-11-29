import os

from scriptcwl import WorkflowGenerator as WFGenerator


class WorkflowGenerator(WFGenerator):
    def __init__(self):
        module_path = os.path.dirname(os.path.realpath(__file__))
        steps_dir = os.path.join(module_path, 'cwl')

        WFGenerator.__init__(self, steps_dir=steps_dir)

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
