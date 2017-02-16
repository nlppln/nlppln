#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.ls"]

inputs:
  dir_in:
    type: Directory
    inputBinding:
      position: 2
stdout: cwl.output.json

outputs:
  files:
    type: File[]
