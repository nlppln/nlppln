"""NLP pipeline utility functionality"""
import os
import shutil
import glob

MODULE_PATH = os.path.dirname(os.path.realpath(__file__))
CWL_PATH = os.path.abspath(os.path.join(MODULE_PATH, 'cwl'))

DEFAULT_DATA_DIR = '{}/.local/share/'.format(os.environ.get('HOME'))
CWL_DATA_DIR_PREFIX = 'commonwl'


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


def copy_cwl_files(from_dir=CWL_PATH):
    """Copy cwl files to a directory where the cwl-runner can find them.

    cwl files are copied to $XDG_DATA_HOME/commonwl/ This is one of the default
    locations where the cwl-runner looks for cwl files.

    Args:
        from_dir (str): Path to directory where to copy files from (default:
            the cwl directory of nlppln).
    """
    cwl_data_dir = os.environ.get('XDG_DATA_HOME')
    if not cwl_data_dir:
        cwl_data_dir = DEFAULT_DATA_DIR

    cwl_data_dir = os.path.join(cwl_data_dir, CWL_DATA_DIR_PREFIX)

    create_dirs(cwl_data_dir)

    cwl_files = glob.glob('{}{}*.cwl'.format(from_dir, os.sep))
    for fi in cwl_files:
        fo = os.path.join(cwl_data_dir, os.path.basename(fi))
        shutil.copy2(fi, fo)


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


if __name__ == '__main__':
    copy_cwl_files()
