#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.save_ner_data"]
arguments:
  - valueFrom: $(runtime.outdir)/ner-statistics.csv
    position: 2

doc: |
  Create csv file with statistics about named entities.

  By editing the csv file, you can control which named entities are replaced or
  removed using `replace-ner.cwl`_.

inputs:
- id: in_files
  type:
    type: array
    items: File
  inputBinding:
    position: 1
outputs:
  - id: ner_statistics
    type: File
    outputBinding:
      glob: "*.csv"
