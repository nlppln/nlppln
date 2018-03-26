#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.ls"]
doc: |
  List files in a directory.

  This command can be used to convert a ``Directory`` into a list of files. This list can be filtered on file name by specifying ``--endswith``.

requirements:
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8

inputs:
  in_dir:
    type: Directory
    inputBinding:
      position: 2
  recursive:
    type: boolean?
    inputBinding:
      prefix: --recursive
  endswith:
    type: string?
    inputBinding:
      prefix: --endswith

stdout: cwl.output.json

outputs:
  out_files:
    type: File[]
