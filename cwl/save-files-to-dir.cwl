cwlVersion: v1.0
class: ExpressionTool

requirements:
  - class: InlineJavascriptRequirement

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
