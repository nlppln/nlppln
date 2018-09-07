#!/usr/bin/env python
import click
import uuid
import tempfile
import patoolib
import shutil
import os

from nlppln.utils import create_dirs, out_file_name, get_files


@click.command()
@click.argument('archive', type=click.Path(exists=True))
@click.option('--remove-dir-structure/--keep-dir-structure', default=False)
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
def archive2dir(archive, remove_dir_structure, out_dir):
    if remove_dir_structure:
        result_dir = os.path.join(out_dir, str(uuid.uuid4()))
        create_dirs(result_dir)

        # make temporary directory
        tempdir = tempfile.mkdtemp()

        # extract archive to temporary directory
        patoolib.extract_archive(archive, outdir=tempdir)

        # copy extracted files to output dir
        files = get_files(tempdir, recursive=True)
        for f in files:
            fo = out_file_name(result_dir, f)
            # don't copy if it's the same file
            if os.path.abspath(f) != fo:
                shutil.copy2(f, fo)

        # remove temporary directory and its contents
        shutil.rmtree(tempdir)
    else:
        # extract archive to temporary directory
        patoolib.extract_archive(archive, outdir=out_dir)


if __name__ == '__main__':
    archive2dir()
