#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.saf_to_txt"]

requirements:
  InitialWorkDirRequirement:
    listing: $(inputs.in_files)
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8

arguments:
  - valueFrom: $(runtime.outdir)
    position: 1

doc: |
  Convert `saf <https://github.com/vanatteveldt/saf>`_ to space separated tokens.

inputs:
  in_files:
    type: File[]
outputs:
  out_files:
    type: File[]
    outputBinding:
      glob: "*.txt"
