#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.frog_to_saf"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: 2

doc: |
  Convert `frog <https://languagemachines.github.io/frog/>`_ csv output to
  `saf <https://github.com/vanatteveldt/saf>`_.

inputs:
  - id: in_files
    type:
      type: array
      items: File
    inputBinding:
      position: 1
outputs:
  - id: saf
    type:
      type: array
      items: File
    outputBinding:
      glob: "*.json"
