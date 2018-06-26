#!/usr/bin/env python
import os
import shutil
import glob
import click

from nlppln.utils import CWL_PATH, create_dirs


def copy_cwl_files(from_dir=CWL_PATH, to_dir=None):
    """Copy cwl files to a directory where the cwl-runner can find them.

    Args:
        from_dir (str): Path to directory where to copy files from (default:
            the cwl directory of nlppln).
        to_dir (str): Path to directory where the files should be copied to
            (e.g., the CWL working directory).
    """
    cwl_files = glob.glob('{}{}*.cwl'.format(from_dir, os.sep))
    # if no files are found, the output directory should not be created
    if len(cwl_files) > 0:
        create_dirs(to_dir)
    for fi in cwl_files:
        fo = os.path.join(to_dir, os.path.basename(fi))
        shutil.copy2(fi, fo)

    return len(cwl_files)


@click.command()
@click.argument('to_dir', type=click.Path())
@click.option('--from_dir', '-f', type=click.Path(exists=True),
              default=CWL_PATH, help='Directory to copy CWL files from '
                                     '(default: the nlppln CWL directory).')
def main(to_dir, from_dir):
    """Copy CWL files."""
    num = copy_cwl_files(from_dir=from_dir, to_dir=to_dir)
    if num > 0:
        click.echo('Copied {} CWL files to "{}".'.format(num, to_dir))
    else:
        msg = 'No CWL files found in "{}". Copied 0 files'.format(from_dir)
        click.echo(msg)


if __name__ == '__main__':
    main(prog_name='nlppln_copy_cwl')
