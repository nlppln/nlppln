# Change Log

## 0.1.0

### Added

#### Commands

- command to convert xml to text (`xml-to-txt.cwl`)
- command to extract word frequencies from saf files (`saf-to-freqs.cwl`)
- command to convert word frequencies to vocabulary ranked by frequency (`freqs.cwl`)
- command to list all files in directory (`ls.cwl`)
- command that takes as input a list of files and returns a list of lists of files (`chunk-list-of-files.cwl`)
- command that tokenizes text using ixa-pipe-tok (`ixa-pipe-tok.cwl`)
- command to download files (`download.cwl`)
- command to rename and copy files (rename-and-copy-files) -> must be used together with cwl-runner option `--relax-path-checks`
- command to convert Word documents (.doc and .docx) to text files using Apache Tika (`apachetika.cwl`)
- command to convert Word documents (.docx) to text files using `docx2txt` (`docx2txt.cwl`)
- command to convert frog output to saf (`frog-to-saf.cwl`)
- commands to frog a single text file and directory of files (`frog-single-text.cwl` and `frog-dir.cwl`)
- command line script to guess the language of all (txt) files in a directory (`language.cwl`)

#### Utils

- command to generate boilerplate python commands and CWL command line tools
- `WorkflowGenerator` class (from `scriptcwl`)
- generate `out_file` name from `in_file` name (using proper file extension)
- copy cwl files to default location (`$XDG_DATA_HOME/commonwl/`) (*CWL files are not yet copied automatically!*)

#### GUI

- functionality for inspecting named entities in text files
