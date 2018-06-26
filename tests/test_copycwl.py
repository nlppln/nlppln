import os

from nlppln.copycwl import copy_cwl_files


def test_copy_cwl_files(fs):
    # Uses pyfakefs http://pyfakefs.org
    fs.create_file('/cwl/step1.cwl')
    fs.create_file('/cwl/step2.cwl')
    fs.create_file('/cwl/step3.cwl')

    assert copy_cwl_files(from_dir='/cwl/', to_dir='/cwl-working-dir') == 3
    assert os.path.exists('/cwl-working-dir/step1.cwl')
    assert os.path.exists('/cwl-working-dir/step2.cwl')
    assert os.path.exists('/cwl-working-dir/step3.cwl')


def test_copy_only_cwl_files(fs):
    # Uses pyfakefs http://pyfakefs.org
    fs.create_file('/cwl/step1.notcwl')

    assert copy_cwl_files(from_dir='/cwl/', to_dir='/cwl-working-dir') == 0


def test_dont_create_directory(fs):
    # Uses pyfakefs http://pyfakefs.org
    fs.create_file('/cwl/step1.notcwl')

    # if no files are copied, the output directory should not be created
    assert not os.path.exists('/cwl-working-dir')
