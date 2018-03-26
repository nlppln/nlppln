#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.save_ner_data"]

requirements:
  InitialWorkDirRequirement:
    listing: $(inputs.in_files)
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8

arguments:
  - valueFrom: $(runtime.outdir)
    position: 1

doc: |
  Create csv file with statistics about named entities.

  By editing the csv file, you can control which named entities are replaced or
  removed using `replace-ner.cwl`_.

inputs:
  in_files:
    type: File[]
  name:
    type: string?
    inputBinding:
      prefix: --name=
      separate: false
outputs:
  ner_statistics:
    type: File
    outputBinding:
      glob: "*.csv"
