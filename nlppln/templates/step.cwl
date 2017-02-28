#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.{{command_name}}"]
{% if meta_out %}
arguments:
  - valueFrom: $(runtime.outdir)/{{meta_out_file}}
    position: 4
{% endif %}

inputs:
{% if meta_in %}
  meta_in:
    type: File
    inputBinding:
      position: 1
{% endif %}
{% if inputs %}
  in_files:
    type:
      type: array
      items: File
    inputBinding:
      position: 2
{% endif %}
{% if outputs %}
  out_dir:
    type: Directory?
    inputBinding:
      prefix: --out_dir=
      separate: false
{% endif %}

outputs:
{% if outputs %}
  out_files:
    type:
      type: array
      items: File
    outputBinding:
      glob: "*.{{extension}}"
{% endif %}
{% if meta_out %}
  metadata_out:
    type: File
    outputBinding:
      glob: "{{meta_out_file}}"
{% endif %}
