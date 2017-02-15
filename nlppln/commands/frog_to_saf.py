#!/usr/bin/env python
import click
import os
import codecs
import json
import datetime

from nlppln.utils import create_dirs, out_file_name


_POSMAP = {"VZ": "P",
           "N": "N",
           "ADJ": "A",
           "LET": ".",
           "VNW": "O",
           "LID": "D",
           "SPEC": "M",
           "TW": "Q",
           "WW": "V",
           "BW": "B",
           "VG": "C",
           "TSW": "I",
           "MWU": "U",
           "": "?",
           }


def parse_frog(lines):
    """
    Interpret the output of the frog parser.
    Input should be an iterable of lines (i.e. the output of call_frog)
    Result is a sequence of dicts representing the tokens
    """
    sid = 0
    for i, line in enumerate(lines):
        if not line:
            # end of sentence marker
            sid += 1
        else:
            parts = line.split("\t")
            tid, token, lemma, morph, pos, conf, ne, _, parent, rel = parts
            if rel:
                rel = (rel, int(parent) - 1)
            result = dict(id=i, sentence=sid, word=token, lemma=lemma,
                          pos=pos, pos_confidence=float(conf),
                          rel=rel)
            if ne != 'O':
                # NER label from BIO tags
                result["ne"] = ne.split('_', 1)[0][2:]
            yield result


def _add_pos1(token):
    """
    Adds a 'pos1' element to a frog token.
    """
    result = token.copy()
    result['pos1'] = _POSMAP[token['pos'].split("(")[0]]
    return result


def frog_to_saf(tokens):
    """
    Convert frog tokens into a new SAF document
    """
    tokens = [_add_pos1(token) for token in tokens]
    module = {'module': "frog",
              "started": datetime.datetime.now().isoformat()}
    return {"header": {'format': "SAF",
                       'format-version': "0.0",
                       'processed': [module]
                       }, "tokens": tokens}


@click.command()
@click.argument('input_files', nargs=-1, type=click.Path(exists=True))
@click.argument('output_dir', nargs=1, type=click.Path())
def frog2saf(input_files, output_dir):
    create_dirs(output_dir)

    for fi in input_files:
        with codecs.open(fi) as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
        saf_data = frog_to_saf(parse_frog(lines))

        head, tail = os.path.split(fi)
        fname = tail.replace(os.path.splitext(tail)[1], '')

        out_file = os.path.join(output_dir, out_file_name(output_dir, fname,
                                                          'json'))
        with codecs.open(out_file, 'wb', encoding='utf-8') as f:
            json.dump(saf_data, f, indent=4)


if __name__ == '__main__':
    frog2saf()
