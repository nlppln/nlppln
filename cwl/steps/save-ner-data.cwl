#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.save_ner_data"]
arguments:
  - valueFrom: $(runtime.outdir)/ner-statistics.csv
    position: 2

inputs:
  - id: dir_in
    type: Directory
    inputBinding:
      position: 1
outputs:
  - id: ner_statistics
    type: File
    outputBinding:
      glob: "*.csv"
