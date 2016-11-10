# start_paper

Use `cookiecutter` to make a folder containing everything you need to start writing an LSST DESC paper (either a journal article or a Note). This follows Jonathan Sick's [`lsst_technote_bootstrap`](https://github.com/lsst-sqre/lsst-technote-bootstrap) method, albeit with a simpler set-up.

## Why should I use this tool?

1. It'll save you some set-up time, which you can spend time writing about science instead.
2. It'll help you comply with the LSST DESC Publication Policy, which places some requirements on papers to state the contributions of its authors.
3. It'll save you some writing time, by automagically writing the author list and acknowledgments, and getting the latex styling right,  for you.

## How do I use it?

You will need to install `cookiecutter`:
```
pip install cookiecutter
```
Then just do:
```
cookiecutter https://github.com/DarkEnergyScienceCollaboration/start_paper.git
```
This will ask you some questions. Here's an example session:
```
first_author [First Last]: Phil Marshall
title [The Title of This Paper]: Twinkles I: A Tiny Sky Survey
description [A very brief description of your paper, for the folder's README. (Once you've 
  typed this, you'll be asked for two more items: a short_title and a serial_number, that 
  will be used to set the paper's folder name. The serial number can be changed later, so 
  choosing 0000 is fine.)]: A short paper describing the Twinkles 1 project, including the 
  design of the survey and the generation of the data, and presenting our results. To be 
  submitted to the AJ.
short_title [paper_title]: twinkles-paper-1
serial_number [0000]: 0001
folder_name [0001-twinkles-paper-1]:
```

The folder that is then produced (silently!) will have the `folder_name` that you entered, and it will contain several pre-configured template files. For LSST DESC Notes, you have a range of format choices available to you: Markdown, rST, ipynb and latex. For latex journal papers, we also provide the AJ style files for convenience, as well as some useful macros. Just choose a format, and start writing in that file!

Don't forget to `git add` and `git commit` the files you edit, in the usual way. You might want to delete the templates you don't use - although if you think you might one day want to upgrade from markdown to latex, or from a Note to a journal article, you could keep those files around.

## Licence, credits etc

People developing this project:
* Phil Marshall [(@drphilmarshall)](https://github.com/DarkEnergyScienceCollaboration/start_paper/issues/new?body=@drphilmarshall)

This is open source software, available under the BSD license. If you are interested in this project, please do drop us a line via the hyperlinked contact names above, or by [writing us an issue](https://github.com/DarkEnergyScienceCollaboration/start_paper/issues?q=).
