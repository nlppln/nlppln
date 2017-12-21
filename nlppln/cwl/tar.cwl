#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: [tar, -xzf]
doc: Extract zipped tar archives.

inputs:
  in_file:
    type: File
    inputBinding:
      position: 1

outputs:
  out:
    type: Directory
    outputBinding:
      glob: "*"
