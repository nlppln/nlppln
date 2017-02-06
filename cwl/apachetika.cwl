#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.apachetika"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: 3

inputs:
- id: in_files
  type:
    type: array
    items: File
  inputBinding:
    position: 2
- id: tika_server
  type: string?
  inputBinding:
    prefix: --tika_server=
    separate: false

outputs:
- id: out_files
  type:
    type: array
    items: File
  outputBinding:
    glob: "*.txt"
