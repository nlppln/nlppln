#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.frog_filter_nes"]

doc: |
  Control which named entities will be removed.

  See `replace-ner.cwl`_.

inputs:
  nerstats:
    type: File
    inputBinding:
      position: 1
  name:
    type: string?
    inputBinding:
      prefix: --name

outputs:
  filtered_nerstats:
    type: File
    outputBinding:
      glob: "*.csv"
