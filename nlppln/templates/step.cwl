#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.{{command_name}}"]
{% if inputs %}
requirements:
  InitialWorkDirRequirement:
    listing: $(inputs.in_files)

arguments:
  - valueFrom: $(runtime.outdir)
    position: 1
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
    type: File[]
{% endif %}
{% if outputs %}
  out_dir:
    type: Directory?
    inputBinding:
      prefix: --out_dir
{% endif %}

outputs:
{% if outputs %}
  out_files:
    type: File[]
    outputBinding:
      glob: "{{glob}}"
{% endif %}
{% if meta_out %}
  metadata_out:
    type: File
    outputBinding:
      glob: "{{meta_out_file}}"
{% endif %}
