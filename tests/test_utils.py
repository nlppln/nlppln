import os

from nlppln.utils import remove_ext, out_file_name, create_dirs


def test_remove_ext_full_path():
    fname = '/home/jvdzwaan/data/test.txt'
    assert remove_ext(fname) == 'test'


def test_remove_ext_filename():
    fname = 'test.txt'
    assert remove_ext(fname) == 'test'


def test_remove_ext_no_ext():
    fname = 'test'
    assert remove_ext(fname) == 'test'


def test_out_file_name_same_ext():
    out_dir = '/home/jvdzwaan/data/'
    fname = 'foo.txt'

    assert out_file_name(out_dir, fname) == '/home/jvdzwaan/data/foo.txt'


def test_out_file_name_path():
    out_dir = '/home/jvdzwaan/data/'
    fname = '/other/path/foo.txt'

    assert out_file_name(out_dir, fname) == '/home/jvdzwaan/data/foo.txt'


def test_out_file_name_change_ext():
    out_dir = '/home/jvdzwaan/data/'
    fname = 'foo.txt'

    out_fname = out_file_name(out_dir, fname, ext='csv')

    assert out_fname == '/home/jvdzwaan/data/foo.csv'


def test_create_dirs_with_file_name(fs):
    # Uses pyfakefs http://pyfakefs.org
    create_dirs('/test/test/test.txt', is_file=True)
    assert os.path.exists('/test/test/')
    assert not os.path.exists('/test/test/test.txt')


def test_create_dirs_with_dir_name(fs):
    # Uses pyfakefs http://pyfakefs.org
    create_dirs('/test/test/')
    assert os.path.exists('/test/test/')
