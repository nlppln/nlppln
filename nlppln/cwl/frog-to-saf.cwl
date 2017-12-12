#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "nlppln.commands.frog_to_saf"]

requirements:
  InitialWorkDirRequirement:
    listing: $(inputs.in_files)

arguments:
  - valueFrom: $(runtime.outdir)
    position: 1

doc: |
  Convert `frog <https://languagemachines.github.io/frog/>`_ csv output to
  `saf <https://github.com/vanatteveldt/saf>`_.

inputs:
  in_files:
    type: File[]

outputs:
  saf:
    type: File[]
    outputBinding:
      glob: "*.json"
