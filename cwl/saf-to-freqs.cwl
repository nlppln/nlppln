#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.freqs"]

arguments:
  - valueFrom: $(runtime.outdir)/freqs.csv
    position: 2

inputs:
- id: in_files
  type:
    type: array
    items: File
  inputBinding:
    position: 1
- id: mode
  type: string?
  inputBinding:
    prefix: --mode
    separate: true

outputs:
  - id: freqs
    type: File
    outputBinding:
      glob: "freqs.csv"
