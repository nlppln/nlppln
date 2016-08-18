#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.{{command_name}}"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: 2

inputs:
  - id: in_files
    type:
      type: array
      items: File
    inputBinding:
      position: 1
outputs:
  - id: {{output_id}}
    type:
      type: array
      items: File
    outputBinding:
      glob: "{{output_binding}}"
