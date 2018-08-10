#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.prettify_xml"]

doc: |
  Pretty print xml file.

  Uses `BeautifulSoup pretty printing <https://www.crummy.com/software/BeautifulSoup/bs4/doc/#pretty-printing>`_.

inputs:
  in_file:
    type: File
    inputBinding:
      position: 2

outputs:
  out_file:
    type: File
    outputBinding:
      glob: "*.xml"
