"""NLP pipeline utility functionality"""
import os

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


def get_files(directory):
    """Return a list of all files in the directory."""
    files_out = []
    for f in os.listdir(directory):
        fi = os.path.join(directory, f)
        if os.path.isfile(fi):
            files_out.append(fi)

    # order alphabetically on file name
    return sorted(files_out)


def split(s):
    return s.split()
