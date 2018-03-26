#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.filter_nes"]

doc: |
  Control which named entities will be removed.

  See `replace-ner.cwl`_.

requirements:
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8
      
inputs:
  nerstats:
    type: File
    inputBinding:
      position: 1
  name:
    type: string?
    inputBinding:
      prefix: --name

outputs:
  filtered_nerstats:
    type: File
    outputBinding:
      glob: "*.csv"
