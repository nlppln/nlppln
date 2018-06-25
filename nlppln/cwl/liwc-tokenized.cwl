#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.liwc"]

doc: |
  Apply `LIWC <http://liwc.net>`_ to a directory of tokenized text files.

  The text files have to contain space separated tokens.

requirements:
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8
      
inputs:
  in_dir:
    type: Directory
    inputBinding:
      position: 1
  liwc_dict:
    type: File
    inputBinding:
      position: 2
  encoding:
    type: string?
    inputBinding:
      prefix: -e

outputs:
  liwc:
    type: File
    outputBinding:
      glob: "*.csv"
