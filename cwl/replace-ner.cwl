#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.replace_ner"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: 3
inputs:
- id: metadata
  type: File
  inputBinding:
    position: 1
- id: in_files
  type:
    type: array
    items: File
  inputBinding:
    position: 2
- id: mode
  type: string?
  inputBinding:
    prefix: --mode=
    separate: false

outputs:
- id: out_files
  type:
    type: array
    items: File
  outputBinding:
    glob: "*.json"
