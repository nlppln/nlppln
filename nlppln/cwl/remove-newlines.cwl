#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.remove_newlines"]

doc: |
  Remove newlines from a text.

requirements:
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8
      
inputs:
  in_file:
    type: File
    inputBinding:
      position: 1
  replacement:
    type: string?
    inputBinding:
      prefix: --replacement

stdout: $(inputs.in_file.nameroot).txt

outputs:
  out_files:
    type: File
    outputBinding:
      glob: $(inputs.in_file.nameroot).txt
