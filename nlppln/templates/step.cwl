#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.{{command_name}}"]
{% if outputs or meta_out -%}
arguments:
{%- endif %}
{% if outputs -%}
  - valueFrom: $(runtime.outdir)
    position: {% if meta_in %}3{% else %}2{% endif %}
{%- endif %}
{% if meta_out -%}
  - valueFrom: $(runtime.outdir)/{{meta_out_file}}
    position: 5
{%- endif %}
inputs:
{% if meta_in -%}
  - id: metadata
  type:
    type: File
  inputBinding:
    position: 1
{%- endif %}
{% if inputs -%}
  - id: in_files
    type:
      type: array
      items: File
    inputBinding:
      position: {% if meta_in %}2{% else %}1{% endif %}
{%- endif %}
outputs:
{% if outputs -%}
  - id: out_files
    type:
      type: array
      items: File
    outputBinding:
      glob: "{{output_binding}}"
{%- endif %}
{% if meta_out -%}
  - id: metadata_out
  type:
    type: File
  outputBinding:
    glob: "{{meta_out_file}}"
{%- endif %}
