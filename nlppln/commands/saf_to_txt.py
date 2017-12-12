#!/usr/bin/env python
import click
import os
import codecs
import json

from nlppln.utils import create_dirs, out_file_name, get_files


@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
@click.option('--mode', default='word')
def saf_to_text(in_dir, out_dir, mode):
    create_dirs(out_dir)

    if mode not in ('word', 'lemma'):
        raise ValueError("Unknown mode: {mode}, "
                         "please choose either word or lemma"
                         .format(**locals()))

    in_files = get_files(in_dir)

    for fi in in_files:
        with codecs.open(fi, encoding='utf-8') as f:
            saf = json.load(f)

        s_id = None
        lines = []

        for t in saf['tokens']:
            if s_id is None:
                s_id = t['sentence']
                sentence = []
            elif t['sentence'] != s_id:
                lines.append(u' '.join(sentence))
                sentence = []
                s_id = t['sentence']

            sentence.append(t[mode])

        out_file = out_file_name(out_dir, os.path.basename(fi), ext='txt')
        with codecs.open(out_file, 'wb', encoding='utf-8') as f:
            f.write(u'\n'.join(lines))
            f.write(u'\n')


if __name__ == '__main__':
    saf_to_text()
