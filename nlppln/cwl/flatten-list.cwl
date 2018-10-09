#!/usr/bin/env cwlrunner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.flatten_list"]
requirements:
  InlineJavascriptRequirement: {}
  InitialWorkDirRequirement:
    listing:
      - entryname: files.json
        entry: $(JSON.stringify(inputs.list))

inputs:
  list:
    type:
      type: array
      items:
        type: array
        items: File


stdout: cwl.output.json

outputs:
  out_files:
    type: File[]
    outputBinding:
      glob: "*"
