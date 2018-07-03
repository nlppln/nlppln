#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.check-utf8"]

doc: |
  Convert text files to utf-8 encoding.

  Uses `BeautifulSoup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_'s
  Unicode, Dammit module to guess the file encoding if it isn't utf-8.

inputs:
  in_dir:
    type: Directory
    inputBinding:
      position: 0
  convert:
    type: boolean?
    inputBinding:
      prefix: --convert

outputs:
  utf8_files:
    type: File[]
