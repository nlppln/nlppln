{% extends 'inputs_to_outputs.cwl' %}
{% block metadata_file %}
  - id: metadata
    type:
      type: File
    inputBinding:
      position: 1
{% endblock %}
