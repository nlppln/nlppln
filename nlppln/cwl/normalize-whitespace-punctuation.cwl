#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.normalize_whitespace_punctuation"]

inputs:
  meta_in:
    type: File
    inputBinding:
      position: 1

outputs:
  metadata_out:
    type: File
    outputBinding:
      glob: "*.txt"
