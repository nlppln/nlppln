#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: ExpressionTool

requirements:
  - class: InlineJavascriptRequirement

doc: |
  Given a list of directories, return a directory that contains all the files in the input directories.

  By default the name of the output directory is `flattened`. You can specify a different name using the `--dir_name` option.

inputs:
  in_dirs: Directory[]
  dir_name:
    type: string?
    default: flattened

outputs:
  out: Directory

expression: |
  ${
    var listing = [];
    inputs.in_dirs.forEach(function(directory){
      directory.listing.forEach(function(f){
        listing.push(f);
      });
    });
    return {"out": {
      "class": "Directory",
      "basename": inputs.dir_name,
      "listing": listing
    } };
  }
