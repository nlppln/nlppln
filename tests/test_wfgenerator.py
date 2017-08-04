import pytest

from nlppln import WorkflowGenerator


class TestWFGenerator(object):
    @pytest.fixture
    def wf(self):
        return WorkflowGenerator()

    def test_steps_in_library(self, wf):
        assert len(wf.steps_library) > 0
