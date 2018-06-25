#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.apachetika"]

doc: |
  Convert Word documents to text using `Apache Tika <https://tika.apache.org/>`_.

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

inputs:
  in_files:
    type: File[]
  tika_server:
    type: string?
    inputBinding:
      prefix: --tika_server=
      separate: false

outputs:
  out_files:
    type:
      type: array
      items: File
    outputBinding:
      glob: "*.txt"
