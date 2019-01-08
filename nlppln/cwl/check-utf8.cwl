#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

requirements:
  InitialWorkDirRequirement:
    listing: $(inputs.in_files)
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8

arguments:
  - valueFrom: $(runtime.outdir)
    position: 0

baseCommand: ["python", "-m", "nlppln.commands.check_utf8"]

doc: |
  Convert text files to utf-8 encoding.

  Uses `BeautifulSoup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_'s
  Unicode, Dammit module to guess the file encoding if it isn't utf-8.

inputs:
  in_files:
    type: File[]
  convert:
    type: boolean?
    inputBinding:
      prefix: --convert

outputs:
  utf8_files:
    type: File[]
