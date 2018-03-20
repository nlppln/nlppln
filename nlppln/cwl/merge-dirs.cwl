#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: ExpressionTool

requirements:
  - class: InlineJavascriptRequirement

doc: |
  Given a list of directories, return a directory that contains all the files in the input directories.

inputs:
  in_dirs: Directory[]

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
      "basename": "merged",
      "listing": listing
    } };
  }
