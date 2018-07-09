#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.delete_empty_files"]
requirements:
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8

inputs:
  in_dir:
    type: Directory
    inputBinding:
      position: 0
outputs:
  out_files:
    type: File[]
    outputBinding:
      glob: "*"
