cwlVersion: v1.0
class: ExpressionTool

requirements:
  - class: InlineJavascriptRequirement

inputs:
  inner_dir: Directory
  outer_dir: Directory

outputs:
  out: Directory

expression: |
  ${
    return {"out": {
      "class": "Directory",
      "basename": inputs.outer_dir.basename + "/" + inputs.inner_dir.basename,
      "listing": inputs.inner_dir.listing
    } };
  }
