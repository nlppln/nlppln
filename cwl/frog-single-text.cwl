#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: frog
arguments: ["-o", $(runtime.outdir)/out.txt]
hints:
  - class: DockerRequirement
    dockerPull: proycon/lamachine
inputs:
  - id: text_in
    type: File
    inputBinding:
      position: 1
      prefix: -t
outputs:
  - id: frogout
    type: File
    outputBinding:
      glob: "*.txt"
