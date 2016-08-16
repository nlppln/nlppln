cwlVersion: v1.0
class: Workflow
inputs:
  tarfile: string
  change_dir: string
  in_files: string

outputs:
  out_files:
    type:
      type: array
      items: File
    outputSource: untar/out_files

steps:
  tar:
    run: ../steps/tar.cwl
    in:
      tarfile: tarfile
      change_dir: change_dir
      in_files: in_files
    out: [tarOut]

  untar:
    run: ../steps/untar.cwl
    in:
      tarfile: tar/tarOut
    out: [out_files]
