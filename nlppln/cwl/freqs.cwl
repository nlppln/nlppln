#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.freqs"]

requirements:
  InitialWorkDirRequirement:
    listing: $(inputs.in_files)

arguments:
  - valueFrom: $(runtime.outdir)
    position: 1

doc: |
  Return a sorted list of word freqencies in the corpus.

arguments:
  - valueFrom: $(runtime.outdir)/freqs.csv
    position: 2

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
