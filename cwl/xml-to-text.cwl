#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.xml_to_text"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: 3

inputs:
- id: in_files
  type: File
  inputBinding:
    position: 2
- id: tag
  type: string?
  inputBinding:
    prefix: --tag=
    separate: false

outputs:
- id: out_files
  type: File
  outputBinding:
    glob: "*.txt"

