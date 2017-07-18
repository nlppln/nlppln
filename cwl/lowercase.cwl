#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.lowercase"]

inputs:
  in_file:
    type: File
    inputBinding:
      position: 1
  out_dir:
    type: Directory?
    inputBinding:
      prefix: --out_dir=
      separate: false

stdout: $(inputs.in_file.nameroot).txt

outputs:
  out_files:
    type: File
    outputBinding:
      glob: $(inputs.in_file.nameroot).txt
