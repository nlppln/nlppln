#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.basic_text_statistics"]

doc: |
  Output a csv file with basic text statistics (#tokens, #sentences).

inputs:
  in_files:
    type:
      type: array
      items: File
    inputBinding:
      position: 2
  out_file:
    type: string
    inputBinding:
      position: 3

outputs:
  metadata_out:
    type: File
    outputBinding:
      glob: $(inputs.out_file)
