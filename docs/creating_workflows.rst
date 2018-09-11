Creating workflows
==================

Pipelines or workflows can be created by writing a Python script:
::

	from nlppln import WorkflowGenerator

	with WorkflowGenerator() as wf:
		txt_dir = wf.add_inputs(txt_dir='Directory')

		frogout = wf.frog_dir(dir_in=txt_dir)
		saf = wf.frog_to_saf(in_files=frogout)
		ner_stats = wf.save_ner_data(in_files=saf)
		new_saf = wf.replace_ner(metadata=ner_stats, in_files=saf)
		txt = wf.saf_to_txt(in_files=new_saf)

		wf.add_outputs(ner_stats=ner_stats, txt=txt)

		wf.save('anonymize.cwl')

This workflow finds named entities in all Dutch text files in a directory. Named
entities are replaced with their type (PER, LOC, ORG). The output consists of
text files and a csv file that contains the named entities that have been replaced.

The workflow creation functionality in ``nlppln`` is provided by a library called
`scriptcwl <https://github.com/NLeSC/scriptcwl>`_. For a more detailed explanation
of how to create workflows, have a look at the
`scriptcwl documentation <http://scriptcwl.readthedocs.io/en/latest/>`_.

Setting workflow inputs
#######################

Wokflow inputs can be added by calling ``add_input()``:
::

	txt_dir = wf.add_inputs(txt_dir='Directory')

The ``add_input()`` method expects a ``name=type`` pair as input parameter.
The pair connects an input name (``txt_dir`` in the example) to a CWL type
(``'Directory'``). An overview of CWL types can be found in the
`specification <http://www.commonwl.org/v1.0/Workflow.html#CWLType>`_.

Check the `scriptcwl documentation <http://scriptcwl.readthedocs.io/en/latest/workflow_inputs.html>`_
to find out how to add optional workflow inputs and default values.

Adding processing steps
#######################

To add a processing step to the workflow, you have to call its method on the ``WorkflowGenerator`` object.
The method expects a list of (key, value) pairs as input parameters. (To find out what inputs a step
needs call ``wf.inputs(<step name>)``. This method prints all the inputs
and their types.) The method returns a list of strings containing output
names that can be used as input for later steps, or that can be connected
to workflow outputs.

For example, to add a step called ``frog-dir`` to the workflow, the
following method must be called:
::

    frogout = wf.frog_dir(dir_in=txt_dir)

In a next step, ``frogout`` can be used as input:
::
    saf = wf.frog_to_saf(in_files=frogout)
    txt = wf.saf_to_txt(in_files=saf)

Etcetera.

Listing steps
#############

To find out what steps are available in ``nlppln`` and to get copy/paste-able
specification of what needs to be typed to add a step to the workflow you can
type:
::

	print(wf.list_steps())

The result is:

.. code-block:: none

	Steps
  	apachetika............... out_files = wf.apachetika(in_files[, tika_server])
  	basic-text-statistics.... metadata_out = wf.basic_text_statistics(in_files, out_file)
  	chunk-list-of-files...... file_list = wf.chunk_list_of_files(chunk_size, in_files)
  	clear-xml-elements....... out_file = wf.clear_xml_elements(element, xml_file)
  	copy-and-rename.......... copy = wf.copy_and_rename(in_file[, rename])
  	docx2txt................. out_files = wf.docx2txt(in_files)
  	download................. out_files = wf.download(urls)
  	freqs.................... freqs = wf.freqs(in_files)
  	frog-dir................. frogout = wf.frog_dir(in_files[, skip])
  	frog-filter-nes.......... filtered_nerstats = wf.frog_filter_nes(nerstats[, name])
  	frog-single-text......... frogout = wf.frog_single_text(in_file)
  	frog-to-saf.............. saf = wf.frog_to_saf(in_files)
  	ixa-pipe-tok............. out_file = wf.ixa_pipe_tok(language, in_file)
  	language................. language_csv = wf.language(dir_in)
  	liwc-tokenized........... liwc = wf.liwc_tokenized(in_dir, liwc_dict[, encoding])
  	lowercase................ out_files = wf.lowercase(in_file)
  	ls....................... out_files = wf.ls(in_dir[, recursive])
  	merge-csv................ merged = wf.merge_csv(in_files[, name])
  	normalize-whitespace-punctuation metadata_out = wf.normalize_whitespace_punctuation(meta_in)
  	pattern-nl............... out_files = wf.pattern_nl(in_files)
  	rename-and-copy-files.... out_files = wf.rename_and_copy_files(in_files)
  	replace-ner.............. out_files = wf.replace_ner(metadata, in_files[, mode])
  	saf-to-freqs............. freqs = wf.saf_to_freqs(in_files[, mode])
  	saf-to-txt............... out_files = wf.saf_to_txt(in_files)
  	save-dir-to-subdir....... out = wf.save_dir_to_subdir(inner_dir, outer_dir)
  	save-files-to-dir........ out = wf.save_files_to_dir(dir_name, in_files)
  	save-ner-data............ ner_statistics = wf.save_ner_data(in_files)
  	textDNA-generate......... json = wf.textDNA_generate(dir_in, mode[, folder_sequences, name_prefix, output_dir])
  	xml-to-text.............. out_files = wf.xml_to_text(in_files[, tag])

	Workflows
  	anonymize................ ner_stats, out_files = wf.anonymize(in_files[, mode])

Setting workflow outputs
########################

When all steps of the workflow have been added, you can specify
workflow outputs by calling ``wf.add_outputs()``:
::

  wf.add_outputs(ner_stats=ner_stats, txt=txt)

In this case the workflow has two outputs, one called ``ner_stats``, which is a
csv file and one called ``txt``, which is a list of text files.

Saving workflows
################

To save a workflow call the ``WorkflowGenerator.save()`` method:
::

  wf.save('anonymize.cwl')

Other options when saving workflows are described in the `scriptcwl
documentation <http://scriptcwl.readthedocs.io/en/latest/saving_workflows.html>`_.
By default, ``nlppln`` saves workflows with embedded steps (``inline=True``).

Adding documentation
####################

To add documentation to your workflow, use the ``set_documentation()`` method:
::

	doc = """Workflow that replaces named entities in text files.

	Input:
		txt_dir: directory containing text files

	Output:
		ner_stats: csv-file containing statistics about named entities in the text files
		txt: text files with named enities replaced
	"""
	wf.set_documentation(doc)

Loading processing steps
########################

``nlppln`` comes with nlp functionality pre-loaded. If you need custom processing
steps, you can create them using `nlppln-gen <https://github.com/nlppln/nlppln-gen>`_.
To be able to add these custom processing steps to you workflow,
you have to load them into the ``WorkflowGenerator``. To load a single CWL file, do:
::

	wf.load(step_file='/path/to/step_or_workflow.cwl')

The ``step_file`` can also be a url.

To load all CWL files in a directory, do:
::

	wf.load(steps_dir='/path/to/dir/with/cwl/steps/')


Using a working directory
#########################

Once you need more functionality than nlppln provides, and start creating your
own processing steps, we recommend using a CWL working directory.
A CWL working directory is a directory containing all available CWL specifications.
To specify a working directory, do:
::

	from nlppln import WorkflowGenerator

  with WorkflowGenerator(working_dir='path/to/working_dir') as wf:
    wf.load(steps_dir='some/path/')
    wf.load(steps_dir='some/other/path/')

    # add inputs, steps and outputs

If you use a working directory when creating pipelines, nlppln copies all CWL files
to the working directory.

To copy these files manually, you can also use the ``nlppln_copy_cwl`` command on the
command line:
::

  nlppln_copy_cwl /path/to/cwl/working/dir

To copy CWL files from a different directory than the one containing the nlppln
CWL files, do:
::

  nlppln_copy_cwl --from_dir /path/to/your/dir/with/cwl/files /path/to/cwl/working/dir


If you use a working directory, please save your workflow using the ``wd=True`` option:
::

  wf.save('workflow.cwl', wd=True)

The workflow is saved in the working directory and then copied to you specified location.
Subsequently, the workflow should be run from the working directory.

Tips and tricks
###############

Create workflows you can run for a single file
----------------------------------------------

If you want to create a workflow that should be applied to each (text) file in a directory,
create a workflow that performs all the steps to a single file. Then, use this workflow
as a subworkflow that is scattered over a list of input files:
::

  from nlppln import WorkflowGenerator

  with WorkflowGenerator(working_dir='path/to/working_dir') as wf:
    wf.load(steps_dir='some/path/')

    in_dir = wf.add_input(in_dir='Directory')

    in_files = wf.ls(in_dir=in_dir)
    processed_files = wf.some_subworkflow(in_file=in_files, scatter='in_file', scatter_method='dotproduct' [, ...])

    wf.add_outputs(out_files=processed_files)


Having a workflow you can run for a single file makes it easier to test the workflow.

Test your workflow by running it for the largest or otherwise most complex file
-------------------------------------------------------------------------------

By running your workflow for the largest or otherwise most complex file, you can
identify problems, such as excessive memory usage, early and/or before running it
for all files in your dataset. There may, of course, still be problems with other
files, but starting analysis with the largest file is easy to do.


Use ``create_chunked_list`` and ``ls_chunk`` to run a workflow for a subset of files
------------------------------------------------------------------------------------

Sometimes running a workflow for all files in a directory takes too long, and you'd like
to run it for subsets of files. Using ``create_chunked_list``, you can create a JSON file
containing a division of the files in a directory in chunks. You can then create a workflow
that, instead of using ``ls`` to list all files in a directory, uses ``ls_chunk`` that
runs the workflow for a single chunk of files.

To create a division of the input files, do:
::

  python -m nlppln.commands.create_chunked_list [--size 500 --out_name output.json] /path/to/directory/with/input/files

The result is a JSON file named ``output.json`` that contains numbered chunks
containing 500 files each.

To run a workflow for a chunk of files, instead of all files in a directory, do:
::

  from nlppln import WorkflowGenerator

  with WorkflowGenerator(working_dir='path/to/working_dir') as wf:
    wf.load(steps_dir='some/path/')

    in_dir = wf.add_input(in_dir='Directory')
    chunks = wf.add_input(chunks='File')
    chunk_name = wf.add_input(name='string')

    in_files = wf.ls_chunk(in_dir=in_dir, chunks=chunks, name=chunk_name)
    processed_files = wf.some_subworkflow(in_file=in_files, scatter='in_file', scatter_method='dotproduct' [, ...])

    wf.add_outputs(out_files=processed_files)
