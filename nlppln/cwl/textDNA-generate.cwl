#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

baseCommand: ["python", "-m", "textdnaDataGen.generate"]

hints:
  - class: DockerRequirement
    dockerPull: nlppln/textdna-create-datasets

requirements:
  EnvVarRequirement:
    envDef:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8
      
doc: |
  Generate data to vizualize using `TextDNA <http://graphics.cs.wisc.edu/Vis/SequenceSurveyor/TextDNA.html>`_.

inputs:
  in_dir:
    type: Directory
    inputBinding:
      position: 1
  mode:
    type: string
    inputBinding:
      position: 3
  folder_sequences:
    type: boolean?
    inputBinding:
      prefix: --folder_sequences
  name_prefix:
    type: string?
    inputBinding:
      prefix: --name-prefix
  output_dir:
    type: Directory?
    inputBinding:
      prefix: --output_dir

outputs:
  json:
    type: File
    outputBinding:
      glob: "*.json"
