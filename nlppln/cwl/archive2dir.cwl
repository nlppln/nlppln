#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.archive2dir"]

doc: |
  Extract archive and recursively put all files in the output directory.

  Uses `Patool <http://wummel.github.io/patool/>_` for extracting archives.

requirements:
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8

arguments:
  - prefix: "-o"
    valueFrom: $(runtime.outdir)

inputs:
  archive:
    type: File
    inputBinding:
      position: 1

outputs:
  out_dir:
    type: Directory
    outputBinding:
      glob: "*"
