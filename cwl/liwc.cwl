#!/usr/bin/env cwlrunner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.liwc"]

inputs:
  liwc_dict:
    type: File
    inputBinding:
      position: 1
  in_files:
    type: File[]
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
      glob: "liwc.csv"
