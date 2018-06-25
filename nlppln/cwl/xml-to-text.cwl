#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.xml_to_text"]

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

doc: Extract text from an XML element and save it to a file.

inputs:
  in_files:
    type: File
  tag:
    type: string?
    inputBinding:
      prefix: --tag=
      separate: false

outputs:
  out_files:
    type: File
    outputBinding:
      glob: "*.txt"
