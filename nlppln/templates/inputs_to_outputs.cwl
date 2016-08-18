#!/usr/bin/env cwl-runner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.{{command_name}}"]
arguments:
  - valueFrom: $(runtime.outdir)
    position: {% if meta_in %}3{% else %}2{% endif %}

inputs:
  {% block metadata_file %}{% endblock %}
  - id: in_files
    type:
      type: array
      items: File
    inputBinding:
      position: {% if meta_in %}2{% else %}1{% endif %}
outputs:
  - id: {{output_id}}
    type:
      type: array
      items: File
    outputBinding:
      glob: "{{output_binding}}"
