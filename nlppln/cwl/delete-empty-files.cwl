#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

requirements:
  InitialWorkDirRequirement:
    listing: $(inputs.in_files)
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8

arguments:
  - valueFrom: $(runtime.outdir)
    position: 0

baseCommand: ["python", "-m", "nlppln.commands.delete_empty_files"]

inputs:
  in_files:
    type: File[]
outputs:
  out_files:
    type: File[]
    outputBinding:
      glob: "*"
