#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlpppln.frog_to_saf"]
arguments:
  - valueFrom: $(runtime.outdir + '/saf/')
    position: 2

inputs:
  - id: dir_in
    type: Directory
    inputBinding:
      position: 1
outputs:
  - id: saf
    type: Directory
    outputBinding:
      glob: "*.json"

requirements:
  - class: InlineJavascriptRequirement
