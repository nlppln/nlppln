#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: Workflow

doc: |
  Replace named entities in a directory of text files.

  Can be used as part of an data anonymization workflow.

inputs:
  txt_dir: Directory
outputs:
  txt:
    type:
      type: array
      items: File
    outputSource: saf-to-txt-1/out_files
  ner_stats:
    type: File
    outputSource: save-ner-data-1/ner_statistics
steps:
  frog-dir:
    run: frog-dir.cwl
    in:
      in_dir: txt_dir
    out:
    - frogout
  frog-to-saf-1:
    run: frog-to-saf.cwl
    in:
      in_files: frog-dir/frogout
    out:
    - saf
  save-ner-data-1:
    run: save-ner-data.cwl
    in:
      in_files: frog-to-saf-1/saf
    out:
    - ner_statistics
  replace-ner-1:
    run: replace-ner.cwl
    in:
      in_files: frog-to-saf-1/saf
      metadata: save-ner-data-1/ner_statistics
    out:
    - out_files
  saf-to-txt-1:
    run: saf-to-txt.cwl
    in:
      in_files: replace-ner-1/out_files
    out:
    - out_files
