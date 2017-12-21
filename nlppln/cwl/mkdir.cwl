#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: [mkdir]
doc: Create directory

inputs:
  dir_name:
    type: string
    inputBinding:
      position: 1

outputs:
  out:
    type: Directory
    outputBinding:
      glob: "*"
