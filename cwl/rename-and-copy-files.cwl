#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.rename-and-copy-files"]
doc: |
  Remove spaces from file names. The renamed files are copied to the current working directory.

  This command must be run with the --relax-path-checks option, because it accepts file names
  with spaces, which CWL normally does not.
arguments:
  - valueFrom: $(runtime.outdir)
    position: 3

inputs:
- id: in_files
  type:
    type: array
    items: File
  inputBinding:
    position: 2

outputs:
- id: out_files
  type:
    type: array
    items: File
  outputBinding:
    glob: "*"
