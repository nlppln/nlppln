#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.command.{{command_name}}"]
{% if outputs or meta_out %}
arguments:
{% endif %}
{% if outputs %}
  - valueFrom: $(runtime.outdir)
    position: 3
{% endif %}
{% if meta_out %}
  - valueFrom: $(runtime.outdir)/{{meta_out_file}}
    position: 4
{% endif %}

inputs:
{% if meta_in %}
- id: meta_in
  type: File
  inputBinding:
    position: 1
{% endif %}
{% if inputs %}
- id: in_files
  type:
    type: array
    items: File
  inputBinding:
    position: 2
{% endif %}

outputs:
{% if outputs %}
- id: out_files
  type:
    type: array
    items: File
  outputBinding:
    glob: "*.{{extension}}"
{% endif %}
{% if meta_out %}
- id: metadata_out
  type: File
  outputBinding:
    glob: "{{meta_out_file}}"
{% endif %}
