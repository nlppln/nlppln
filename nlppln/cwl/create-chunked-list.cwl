#!/usr/bin/env cwlrunner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.create_chunked_list"]

inputs:
  in_dir:
    type: Directory
    inputBinding:
      position: 1
  out_name:
    type: string?
    inputBinding:
      prefix: --out_name

outputs:
  chunks:
    type: File
    outputBinding:
      glob: "*.json"
