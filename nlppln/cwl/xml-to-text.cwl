#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.xml_to_text"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: 3

doc: Extract text from an XML element and save it to a file.

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
