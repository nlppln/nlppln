#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: ExpressionTool
requirements:
  InlineJavascriptRequirement: {}

inputs:
  in_files:
    type: File[]
  chunk_size:
    type: int

expression: |
  ${
  var files = [];
  var chunk = [];
  inputs.in_files.forEach(function(f){
    chunk.push(f);
    if(chunk.length==inputs.chunk_size){
      files.push(chunk);
      chunk = [];
    }
  });
  if(chunk.length > 0){
    files.push(chunk);
  }
  return {'file_list': files}; }

outputs:
  file_list:
    type:
      type: array
      items:
        type: array
        items: File
