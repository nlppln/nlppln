#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.lowercase"]

doc: |
  Lowercase a text.

inputs:
  in_file:
    type: File
    inputBinding:
      position: 1

stdout: $(inputs.in_file.nameroot).txt

outputs:
  out_files:
    type: File
    outputBinding:
      glob: $(inputs.in_file.nameroot).txt
