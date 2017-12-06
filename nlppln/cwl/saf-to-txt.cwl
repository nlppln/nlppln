#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.saf_to_txt"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: 2

doc: |
  Convert `saf <https://github.com/vanatteveldt/saf>`_ to space separated tokens.

inputs:
- id: in_files
  type:
    type: array
    items: File
  inputBinding:
    position: 1
outputs:
- id: out_files
  type:
    type: array
    items: File
  outputBinding:
    glob: "*.txt"
