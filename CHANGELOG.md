# Change Log

## Unreleased

### Added

- Command to extract tar.gz files (`tar.cwl`)
- Command to create directories (`mkdir.cwl`)

### Changed

- Remove erroneous arguments section from `freqs.cwl`

## 0.3.0

### Added

- CWL files for NLP functionality (so they don't have to be downloaded separately)
- Dockerfile to run nlppln on Windows
- First tests
- Python 3 support
- By default, save workflows using working directory
- Documentation on [Read the Docs](http://nlppln.readthedocs.io/en/latest/)
- Command to copy and rename files (`copy-and-rename-files.cwl`)
- Command to generate data for TextDNA visualization (`textDNA-generate.cwl`)
- Command to normalize whitespace and punctuation in text files (`normalize-whitespace-punctuation.cwl`)
- Command to run LIWC on tokenized text (`liwc_tokenized.cwl`)
- Command to save a directory to a subdirectory (`save-dir-to-subdir.cwl`)
- Command to save a list of files to a directory (`save-files-to-dir.cwl`)
- Command to merge csv files (`merge-csv.cwl`)
- Command to filter Named Entities extracted with frog (`frog-filter-nes.cwl`)
- Command to list al files in a directory (`ls.cwl`)
- Command to lowercase a text (`lowercase.cwl`)
- Command to clear xml elements (`clear-xml-elements.cwl`)

### Changed

- Command `saf_to_text.py` (`saf-to-text.cwl`) outputs space separated sentences
- Give Python commands a meaningful name (#5)
- Use `InitialWorkDirRequirement` instead of list of input files (#1 #16)

### Removed

- GUI (users are recommended to use Juyter notebooks for inspection and analysis tasks)
- Functionality to generate boilerplate Python commands and CWL files (moved to https://github.com/nlppln/nlppln-gen)
- Command to create a file list (use cwltool option `--make-template` instead) (#14)

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
