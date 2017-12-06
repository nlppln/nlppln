#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: frog
arguments: ["-o", $(inputs.in_file.nameroot).out]
hints:
  - class: DockerRequirement
    dockerPull: proycon/lamachine

doc: |
  `Frog <https://languagemachines.github.io/frog/>`_ a single text file.

inputs:
  in_file:
    type: File
    inputBinding:
      position: 1
      prefix: -t
outputs:
  frogout:
    type: File
    outputBinding:
      glob: "$(inputs.in_file.nameroot).out"
