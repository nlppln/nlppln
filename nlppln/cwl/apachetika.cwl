#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.apachetika"]

inputs:
  in_files:
    type:
      type: array
      items: File
    inputBinding:
      position: 2
  tika_server:
    type: string?
    inputBinding:
      prefix: --tika_server=
      separate: false

outputs:
  out_files:
    type:
      type: array
      items: File
    outputBinding:
      glob: "*.txt"
