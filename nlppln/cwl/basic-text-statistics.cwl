#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.basic_text_statistics"]

doc: |
  Output a csv file with basic text statistics (#tokens, #sentences).

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

inputs:
  in_files:
    type: File[]
  out_file:
    type: string
    inputBinding:
      position: 3

outputs:
  metadata_out:
    type: File
    outputBinding:
      glob: $(inputs.out_file)
