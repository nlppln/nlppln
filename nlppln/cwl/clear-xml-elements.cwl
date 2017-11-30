#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.clear_xml_elements"]

inputs:
  xml_file:
    type: File
    inputBinding:
      position: 1
  element:
    type:
      type: array
      items: string
      inputBinding:
        prefix: -e

outputs:
  out_file:
    type: File
    outputBinding:
      glob: "*.xml"
