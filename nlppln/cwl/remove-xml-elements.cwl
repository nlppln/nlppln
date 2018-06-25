#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.remove_xml_elements"]

doc: |
  Remove specified XML elements from XML file.

requirements:
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8
      
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
