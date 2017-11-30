#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.pattern_nl"]

inputs:
  in_files:
    type:
      type: array
      items: File
    inputBinding:
      position: 2

outputs:
  out_files:
    type:
      type: array
      items: File
    outputBinding:
      glob: "*.json"
