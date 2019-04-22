#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: Workflow
requirements:
- class: ScatterFeatureRequirement
inputs:
  in_dir: Directory
  language:
    default: nl
    type: string
  out_name:
    default: text_stats.csv
    type: string
outputs:
  stats:
    outputSource: basic-text-statistics/metadata_out
    type: File
steps:
  ls:
    run: ls.cwl
    in:
      in_dir: in_dir
    out:
    - out_files
  pattern:
    run: https://raw.githubusercontent.com/nlppln/pattern-docker/master/pattern.cwl
    in:
      in_file: ls/out_files
      language: language
    out:
    - saf
    scatter:
    - in_file
  basic-text-statistics:
    run: basic-text-statistics.cwl
    in:
      in_files: ls/out_files
      out_name: out_name
    out:
    - metadata_out
