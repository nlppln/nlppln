#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.copy_and_rename"]
doc: |
  Copy a file and optionally rename it.

  File renaming options are: ``copy`` (don't rename), ``spaces`` (remove
  spaces, default), and ``random`` (generate a random file name. The file
  extension is copied too.) If the renaming option is spaces, this tool must be
  run with the ``--relax-path-checks`` option, because it accepts file names
  with spaces, which CWL normally does not accept.

requirements:
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8
      
inputs:
  in_file:
    type: File
    inputBinding:
      position: 1
  rename:
    type: string?
    inputBinding:
      prefix: --rename

outputs:
  copy:
    type: File
    outputBinding:
      glob: "*"
