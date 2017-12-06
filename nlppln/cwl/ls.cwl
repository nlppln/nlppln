#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.ls"]
doc: |
  List files in a directory.

  This command can be used to convert a ``Directory`` into a list of files.

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
