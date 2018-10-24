#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: [yamlreader]

inputs:
  in_files:
    type: File[]
    inputBinding:
      position: 1
  out_name:
     type: string

stdout: $(inputs.out_name)

outputs:
  out_file:
    type: File
    outputBinding:
      glob: "$(inputs.out_name)"
