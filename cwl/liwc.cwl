#!/usr/bin/env cwlrunner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.liwc"]

inputs:
  in_dir:
    type: Directory
    inputBinding:
      position: 1
  liwc_dict:
    type: File
    inputBinding:
      position: 2
  encoding:
    type: string?
    inputBinding:
      prefix: -e

outputs:
  liwc:
    type: File
    outputBinding:
      glob: "*.csv"
