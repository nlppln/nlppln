#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: [tar, zcf]
arguments:
inputs:
  - id: tarfile
    type: string
    inputBinding:
      position: 1
  - id: change_dir
    type: string
    inputBinding:
      prefix: -C
      position: 2
  - id: in_files
    type: string
#      type: array
#      items: string
    inputBinding:
      position: 3

outputs:
  - id: tarOut
    type: File
    outputBinding:
      glob: $(inputs.tarfile)
