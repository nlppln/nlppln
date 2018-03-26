#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.replace_ner"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: 3

doc: |
  Replace named entities in `saf <https://github.com/vanatteveldt/saf>`_ files.

  Named entities can be replaced with their type or deleted.

requirements:
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8
      
inputs:
- id: metadata
  type: File
  inputBinding:
    position: 1
- id: in_files
  type:
    type: array
    items: File
  inputBinding:
    position: 2
- id: mode
  type: string?
  inputBinding:
    prefix: --mode=
    separate: false

outputs:
- id: out_files
  type:
    type: array
    items: File
  outputBinding:
    glob: "*.json"
