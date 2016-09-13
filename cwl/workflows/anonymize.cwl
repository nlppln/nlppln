cwlVersion: v1.0
class: Workflow
inputs:
  txt-dir: Directory

outputs:
  ner_stats:
    type: File
    outputSource: save-ner-data/ner_statistics

  out_files:
    type:
      type: array
      items: File
    outputSource: saf-to-txt/out_files

steps:
  frog-ner:
    run: ../steps/frog-dir.cwl
    in:
      dir_in: txt-dir
    out: [frogout]

  frog-to-saf:
    run: ../steps/frog-to-saf.cwl
    in:
      in_files: frog-ner/frogout
    out: [saf]

  save-ner-data:
    run: ../steps/save-ner-data.cwl
    in:
      in_files: frog-to-saf/saf
    out: [ner_statistics]

  replace-ner:
    run: ../steps/replace-ner.cwl
    in:
      metadata: save-ner-data/ner_statistics
      in_files: frog-to-saf/saf
    out: [out_files]

  saf-to-txt:
    run: ../steps/saf-to-txt.cwl
    in:
      in_files: replace-ner/out_files
    out: [out_files]
