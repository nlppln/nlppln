#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.guess_language"]
arguments:
  - valueFrom: $(runtime.outdir)/language.csv
    position: 2

inputs:
  - id: dir_in
    type: Directory
    inputBinding:
      position: 1
outputs:
  - id: language_csv
    type: File
    outputBinding:
      glob: "*.csv"
