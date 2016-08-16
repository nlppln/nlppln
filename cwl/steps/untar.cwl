#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: [tar, xf]
arguments:
inputs:
  - id: tarfile
    type: File
    inputBinding:
      position: 1
outputs:
  - id: out_files
    type:
      type: array
      items: File
    outputBinding:
      glob: "*"
