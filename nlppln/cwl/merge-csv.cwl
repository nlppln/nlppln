#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.merge_csv"]
requirements:
  InitialWorkDirRequirement:
    listing: $(inputs.in_files)

arguments:
  - valueFrom: $(runtime.outdir)
    position: 1

inputs:
  in_files:
    type: File[]
  name:
    type: string?
    default: merged.csv
    inputBinding:
      prefix: --name=
      separate: false

outputs:
  merged:
    type: File
    outputBinding:
      glob: $(inputs.name)
