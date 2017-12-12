#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: frog
arguments:
  - prefix: --outputdir=
    separate: false
    valueFrom: $(runtime.outdir)

requirements:
  - class: DockerRequirement
    dockerPull: proycon/lamachine

doc: |
  `Frog <https://languagemachines.github.io/frog/>`_ a directory of text files.

inputs:
  in_dir:
    type: Directory
    inputBinding:
      prefix: --testdir=
      separate: false

  skip:
    type: string?
    inputBinding:
      position: 2
      prefix: --skip=
      separate: false
outputs:
  frogout:
    type: File[]
    outputBinding:
      glob: "*.out"
