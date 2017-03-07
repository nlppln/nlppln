#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.basic_text_statistics"]

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
