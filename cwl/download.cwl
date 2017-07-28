#!/usr/bin/env cwlrunner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.download"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: 3

inputs:
- id: urls
  type:
    type: array
    items: string
  inputBinding:
    position: 2

outputs:
- id: out_files
  type:
    type: array
    items: File
  outputBinding:
    glob: "*"
