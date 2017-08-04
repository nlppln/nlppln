#!/usr/bin/env cwlrunner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.frog_filter_nes"]

inputs:
  nerstats:
    type: File
    inputBinding:
      position: 1
  name:
    type: string?
    inputBinding:
      prefix: --name
  out_dir:
    type: Directory?
    inputBinding:
      prefix: --out_dir

outputs:
  filtered_nerstats:
    type: File
    outputBinding:
      glob: "*.csv"
