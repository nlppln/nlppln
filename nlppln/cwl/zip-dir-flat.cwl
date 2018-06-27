#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["zip", "-jr"]
doc: |
  Compress a directory into a zip archive.

  All structure is removed from the input directory. So, if you unzip the archive,
  you get a flat list of files.

inputs:
  in_dir:
    type: Directory
    inputBinding:
      position: 1
  zip_name:
    type: string
    default: result.zip
    inputBinding:
      position: 0


outputs:
  zip_file:
    type: File
    outputBinding:
      glob: "*"
