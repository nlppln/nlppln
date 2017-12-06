#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.pattern_nl"]

doc: |
  Parse Dutch text using `pattern.nl <https://www.clips.uantwerpen.be/pages/pattern-nl>`_.

  Does lemmatization and named entity recognition.

  Output is `saf <https://github.com/vanatteveldt/saf>`_.

inputs:
  in_files:
    type:
      type: array
      items: File
    inputBinding:
      position: 2

outputs:
  out_files:
    type:
      type: array
      items: File
    outputBinding:
      glob: "*.json"
