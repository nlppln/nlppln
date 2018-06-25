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
  Return csv file wit a ranked list of (word, pos) pairs.

  The list can be of (word, pos) pairs of (lemma, pos) pairs.

inputs:
  in_files:
    type: File[]
  name:
    type: string?
    default: freqs.csv
    inputBinding:
      prefix: --name=
      separate: false
  mode:
    type: string?
    inputBinding:
      prefix: --mode
      separate: true

outputs:
  freqs:
    type: File
    outputBinding:
      glob: "*.csv"
