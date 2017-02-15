#!/usr/bin/env python
import click
import os
import codecs
import json


@click.command()
@click.argument('input_files', nargs=-1, type=click.Path(exists=True))
@click.argument('output_dir', nargs=1, type=click.Path())
@click.option('--mode', default='word')
def command(input_files, output_dir, mode):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if mode not in ('word', 'lemma'):
        raise ValueError("Unknown mode: {mode}, "
                         "please choose either word or lemma"
                         .format(**locals()))

    for fi in input_files:
        with codecs.open(fi, encoding='utf-8') as f:
            saf = json.load(f)

        s_id = None
        lines = []

        for t in saf['tokens']:
            if s_id is None:
                s_id = t['sentence']
                sentence = []
            elif t['sentence'] != s_id:
                lines.append(u''.join(sentence).strip())
                sentence = []
                s_id = t['sentence']

            if t.get('pos1') == '.':
                sentence.append(t[mode])
            else:
                sentence.append(u' {}'.format(t[mode]))

        head, tail = os.path.split(fi)
        fname = tail.replace(os.path.splitext(tail)[1], '')

        out_file = os.path.join(output_dir, '{}.txt'.format(fname))
        with codecs.open(out_file, 'wb', encoding='utf-8') as f:
            f.write(u'\n'.join(lines))
            f.write(u'\n')


if __name__ == '__main__':
    command()
