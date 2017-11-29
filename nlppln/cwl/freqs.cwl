#!/usr/bin/env cwl-runner
cwlVersion: v1.0
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

outputs:
  - id: freqs
    type: File
    outputBinding:
      glob: "freqs.csv"
