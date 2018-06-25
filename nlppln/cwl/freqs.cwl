#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.freqs"]

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
  Return a sorted list of word frequencies in the corpus.

  The corpus should consist of files containing space-separated tokens.

inputs:
  in_files:
    type: File[]
  name:
    type: string?
    default: freqs.csv
    inputBinding:
      prefix: --name=
      separate: false

outputs:
  freqs:
    type: File
    outputBinding:
      glob: "*.csv"
