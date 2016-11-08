import os

from scriptcwl import WorkflowGenerator as WFGenerator


class WorkflowGenerator(WFGenerator):
    def __init__(self):
        module_path = os.path.dirname(os.path.realpath(__file__))
        steps_dir = os.path.join(module_path, '../cwl/')
        steps_dir = os.path.realpath(steps_dir)

        WFGenerator.__init__(self, steps_dir=steps_dir)
