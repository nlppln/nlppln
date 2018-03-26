#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.merge_csv"]
requirements:
  InitialWorkDirRequirement:
    listing: $(inputs.in_files)
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8

arguments:
  - valueFrom: $(runtime.outdir)
    position: 1

doc: Merge csv files (with the same header) into a single csv file.

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
