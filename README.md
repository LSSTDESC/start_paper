# start_paper

Use `cookiecutter` to make a folder containing everything you need to start writing an LSST DESC paper (either a journal article or a Note). This follows Jonathan Sick's [`lsst_technote_bootstrap`](https://github.com/lsst-sqre/lsst-technote-bootstrap) method, albeit with a simpler set-up.

[![Build Status](https://travis-ci.org/DarkEnergyScienceCollaboration/start_paper.svg?branch=master)](https://travis-ci.org/DarkEnergyScienceCollaboration/start_paper)

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
authors [First Author, Second Author, Another Author]: Phil Marshall, Alex Drlica-Wagner, Heather Kelly, Jonathan Sick
title [The Title of This Paper]: How to Start Writing an LSST DESC Paper
description [A very brief description of your paper, for the folder's README. (Once you've typed this, you'll be asked for three more items: a short_title, a serial_number, and the project repo name. These will then be used to set the paper's folder name. The serial number can be changed later, so choosing 0000 is fine.)]: A short paper describing the "start_paper" project, including the cookiecutter mechanism and the various templates.
short_title [paper_title]: intro
serial_number [0000]: 0000
repo_name [ProjectName]: start_paper
folder_name [desc-0000-start_paper-intro]:
```

The folder that is then produced (silently!) will have the `folder_name` that you entered, and it will contain several pre-configured template files. For LSST DESC Notes, you have a range of format choices available to you: Markdown, rST, ipynb and latex. For latex journal papers, we also provide the AJ style files for convenience, as well as some useful macros. Just choose a format, and start writing in that file!

Don't forget to `git add` and `git commit` the files you edit, in the usual way. You might want to delete the templates you don't use - although if you think you might one day want to upgrade from markdown to latex, or from a Note to a journal article, you could keep those files around.

## Licence, credits etc

People developing this project:
* Phil Marshall [(@drphilmarshall)](https://github.com/drphilmarshall)
* Alex Drlica-Wagner [(@kadrlica)](https://github.com/kadrlica)
* Heather Kelly [(@heather999)](https://github.com/heather999)
* Jonathan Sick [(@jonathansick)](https://github.com/jonathansick)

This is open source software, available under the BSD license. If you are interested in this project, please do drop us a line via the hyperlinked contact names above, or by [writing us an issue](https://github.com/DarkEnergyScienceCollaboration/start_paper/issues?q=).
