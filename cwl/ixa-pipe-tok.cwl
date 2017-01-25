#!/usr/bin/env cwlrunner
cwlVersion: cwl:v1.0
class: CommandLineTool
baseCommand: ["java", "-jar", "/ixa-pipe-tok-exec.jar", "tok"]

hints:
  - class: DockerRequirement
    dockerPull: nlppln/ixa-pipe-tok-docker:1.8.5

inputs:
- id: language
  type: string
  inputBinding:
    prefix: -l
- id: in_file
  type: File

stdin: $(inputs.in_file.path)
stdout: $(inputs.in_file.nameroot).xml

outputs:
- id: out_file
  type: File
  outputBinding:
    glob: $(inputs.in_file.nameroot).xml
