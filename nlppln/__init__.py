import os

from wfgenerator import WorkflowGenerator
from commnds import *

__version__ = '0.0.0'

MODULE_PATH = os.path.dirname(os.path.realpath(__file__))
CWL_PATH = os.path.abspath(os.path.join(MODULE_PATH, '../cwl'))
