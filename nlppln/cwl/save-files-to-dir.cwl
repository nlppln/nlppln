#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: ExpressionTool

requirements:
  - class: InlineJavascriptRequirement

doc: |
  Save a list of files to a directory.

inputs:
  in_files: File[]
  dir_name: string

outputs:
  out: Directory

expression: |
  ${
    return {"out": {
      "class": "Directory",
      "basename": inputs.dir_name,
      "listing": inputs.in_files
    } };
  }
