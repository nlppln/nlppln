#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: frog
arguments:
  - prefix: --outputdir=
    separate: false
    valueFrom: $(runtime.outdir)
hints:
  - class: DockerRequirement
    dockerPull: proycon/lamachine
inputs:
  - id: dir_in
    type: Directory
    inputBinding:
      position: 1
      prefix: --testdir=
      separate: false
  - id: skip
    type: string?
    inputBinding:
      position: 2
      prefix: --skip=
      separate: false
outputs:
  - id: frogout
    type:
      type: array
      items: File
    outputBinding:
      glob: "*.out"
