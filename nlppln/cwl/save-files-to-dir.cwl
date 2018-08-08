#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: ExpressionTool

requirements:
  - class: InlineJavascriptRequirement

doc: |
  Save a list of files to a directory.

  If the ``dir_name`` is not specified, it is set to the string before the rightmost - of the ``nameroot`` of the first input file
  (e.g., ``input-file-1-0000.txt`` becomes ``input-file-1``). If the file name does not contain a -, the ``nameroot`` is used (e.g.
  ``input.txt`` becomes ``input``).

inputs:
  in_files: File[]
  dir_name: string?

outputs:
  out: Directory

expression: |
  ${
    var dir_name;
    if (inputs.dir_name == null ){
       var parts = inputs.in_files[0].nameroot.split('-');
       if (parts.length > 1){
         dir_name = parts.slice(0, -1).join('-')
       } else {
         dir_name = parts[0]
       }

    } else {
      dir_name = inputs.dir_name;
    }
    return {"out": {
      "class": "Directory",
      "basename": dir_name,
      "listing": inputs.in_files
    } };
  }
