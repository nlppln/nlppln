"""NLP pipeline utility functionality"""
import os
import itertools
import codecs
import six

from bs4 import BeautifulSoup


MODULE_PATH = os.path.dirname(os.path.realpath(__file__))
CWL_PATH = os.path.abspath(os.path.join(MODULE_PATH, 'cwl'))


def remove_ext(fname):
    """Removes the extension from a filename
    """
    bn = os.path.basename(fname)
    return os.path.splitext(bn)[0]


def create_dirs(fname, is_file=False):
    """Create (output) directories if they don't exist

    Removes the file name part if is_file is set to True.
    """
    fname = os.path.abspath(fname)
    if is_file:
        fname = os.path.dirname(fname)

    if not os.path.exists(fname):
        os.makedirs(fname)


def out_file_name(out_dir, fname, ext=None):
    """Return path of output file, given a directory, file name and extension.

    If fname is a path, it is converted to its basename.

    Args:
        out_dir (str): path to the directory where output should be written.
        fname (str): path to the input file.
        ext (str): file extension of the output file (defaults to None).

    Returns:
        str: out_dir + fname with extension replaced. If `ext` is `None`, the
            original extension is kept.
    """
    if ext is None:
        return os.path.join(out_dir, os.path.basename(fname))

    fname = remove_ext(fname)
    return os.path.join(out_dir, '{}.{}'.format(fname, ext))


def cwl_file(fname):
    return {'class': 'File', 'path': fname}


def get_files(directory, recursive=False):
    """Return a list of all files in the directory."""
    files_out = []
    if recursive:
        for root, dirs, files in os.walk(os.path.abspath(directory)):
            files = [os.path.join(root, f) for f in files]
            files_out.append(files)
        files_out = list(itertools.chain(*files_out))
    else:
        files_out = [os.path.join(directory, f) for f in os.listdir(directory)]
        files_out = list(filter(lambda f: os.path.isfile(f), files_out))

    # order alphabetically on file name
    return sorted(files_out)


def split(s):
    return s.split()


def read_xml(fname):
    with codecs.open(fname, encoding='utf-8') as f:
        xml = f.read()
    return BeautifulSoup(xml, 'xml')


def write_xml(soup, fname):
    with codecs.open(fname, 'wb', encoding='utf-8') as f:
        if six.PY2:
            # six.u doesn't work in Python 2 with non-ascii text
            # See https://pythonhosted.org/six/#six.u
            f.write(unicode(soup))
        else:
            f.write(str(soup))
