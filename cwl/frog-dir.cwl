#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: frog
arguments:
  - prefix: --outputdir=
    separate: false
    valueFrom: $(runtime.outdir)
  - prefix: --testdir=
    separate: false
    valueFrom: $(runtime.outdir)
hints:
  - class: DockerRequirement
    dockerPull: proycon/lamachine
requirements:
  InitialWorkDirRequirement:
    listing: $(inputs.in_files)
inputs:
  in_files: File[]
  skip:
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
