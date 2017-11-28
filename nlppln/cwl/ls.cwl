#!/usr/bin/env cwlrunner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.ls"]

inputs:
  in_dir:
    type: Directory
    inputBinding:
      position: 2
  recursive:
    type: boolean?
    inputBinding:
      prefix: --recursive

stdout: cwl.output.json

outputs:
  out_files:
    type: File[]
