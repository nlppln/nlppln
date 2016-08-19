"""NLP pipeline utility functionality"""
import os

def remove_ext(fname):
    """Removes the extension from a filename
    """
    bn = os.path.basename(fname)
    return os.path.splitext(bn)[0]


def create_dirs(fname):
    """Create (output) directories if they don't exist
    """
    fname = os.path.dirname(os.path.abspath(fname))

    if not os.path.exists(fname):
        os.makedirs(fname)

def out_file_name(out_dir, fname, ext):
    fname = remove_ext(fname)
    return os.path.join(out_dir, '{}.{}'.format(fname, ext))
