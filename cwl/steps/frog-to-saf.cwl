#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.frog_to_saf"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: 2

inputs:
  - id: dir_in
    type: Directory
    inputBinding:
      position: 1
outputs:
  - id: saf
    type:
      type: array
      items: File
    outputBinding:
      glob: "*.json"
