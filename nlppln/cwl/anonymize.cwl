cwlVersion: v1.0
class: Workflow

inputs:
  in_files: File[]
  mode: string?

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
    run: frog-dir.cwl
    in:
      in_files: in_files
    out: [frogout]

  frog-to-saf:
    run: frog-to-saf.cwl
    in:
      in_files: frog-ner/frogout
    out: [saf]

  save-ner-data:
    run: save-ner-data.cwl
    in:
      in_files: frog-to-saf/saf
    out: [ner_statistics]

  filter-nes:
    run: frog-filter-nes.cwl
    in:
      nerstats: save-ner-data/ner_statistics
    out: [filtered_nerstats]

  replace-ner:
    run: replace-ner.cwl
    in:
      metadata: filter-nes/filtered_nerstats
      in_files: frog-to-saf/saf
      mode: mode
    out: [out_files]

  saf-to-txt:
    run: saf-to-txt.cwl
    in:
      in_files: replace-ner/out_files
    out: [out_files]
