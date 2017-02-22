# start_paper

Use `cookiecutter` to make a folder containing everything you need to start writing an LSST DESC paper (either a journal article or a Note). This follows Jonathan Sick's [`lsst_technote_bootstrap`](https://github.com/lsst-sqre/lsst-technote-bootstrap) method, albeit with a simpler set-up.

[![Build Status](https://travis-ci.org/DarkEnergyScienceCollaboration/start_paper.svg?branch=master)](https://travis-ci.org/DarkEnergyScienceCollaboration/start_paper)

## Why should I use this tool?

1. It'll save you some paper set-up time.
2. It'll help you comply with the LSST DESC Publication Policy, which places some requirements on papers to state the contributions of its authors.
3. It'll save you some writing time, by automagically constructing the author list and acknowledgments, and getting the latex styling right,  for you.

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
author [Initial author]: Phil Marshall
affiliation [Initial author's affiliation]: SLAC National Accelerator Laboratory, Menlo Park, CA 94025
email [Initial author's email address]: pjm@slac.stanford.edu
title [The Title of This Paper]: How to Start Writing an LSST DESC Paper
description [A very brief description of your paper, for the folder's README. (Once you've typed this, you'll be asked for three more items:  the project repo name, a serial number (just choose 0000, it'll get changed later), and a short title (that doesn't contain the repo name). These will then be used to set the paper's folder name, for you to accept or modify. Finally, you'll be asked to choose your Note's format, from [tex/apj/mnras/prl/prd/ipynb/md/rst]. You can always change your mind later, and it's easy to convert a tex Note into a journal paper with the start_paper make command.]: A short paper describing the \texttt{start\_paper} project, including the \texttt{cookiecutter} mechanism and the various templates.
repo_name [ProjectName]: start_paper
serial_number [0000]: 0000
short_title [paper_title]: intro
folder_name [desc-0000-start_paper-intro]:
default_format [tex]: tex
```


The folder that is then produced (silently!) will have the `folder_name` that you entered, and it will contain several pre-configured template files. For LSST DESC Notes, you have a range of format choices available to you: `md`, `rst`, `ipynb` and `tex`.

For latex journal papers, we provide a number of style files for convenience, as well as some useful macros. Just choose a format (`apj`, `apjl`, `mnras`, `prd`, `prl`, `tex`, `md`, `rst`, `ipynb`) and start writing in that file! Templates for all formats are provided, so you can switch to a different one at any time. For example, your `default_format` might be `tex`, but `make apjl` will produce a PDF of your note using the ApJL style file.

> For now, `make ipynb` still causes the `main.tex` file to be compiled. In future, we'll enable compilation of PDF or HTML from IPython notebooks.

Don't forget to `git add` and `git commit` the files you edit, in the usual way. You might want to delete the templates you don't use - although if you think you might one day want to upgrade from markdown to latex, or from a Note to a journal article, you could keep those files around.

## What does it do about author lists, contributions etc?

`make` generates two new latex files, an author list in the appropriate style
in `authors.tex`, and a simple listing of author contributions for the
acknowledgements in `contributions.tex`. This is carried out using the python
program [`mkauthlist`](https://github.com/DarkEnergySurvey/mkauthlist) which
the `Makefile` will attempt to install for you. This feature is somewhat
experimental: if you hit problems, please [write us an
issue](https://github.com/DarkEnergyScienceCollaboration/start_paper/issues).
To change the author list and contribution statements, please edit the
`authors.csv` file. Eventually, this file will be automatically obtained from
the LSST DESC Publication System, but for now we can track our own
contributions manually in this way. If you are writing a Note in `markdown`,
`rst` or `ipynb` format, you'll need to add your contribution list to your main
file by hand.


## Licence, credits etc

People developing this project:
* Phil Marshall [(@drphilmarshall)](https://github.com/drphilmarshall)
* Alex Drlica-Wagner [(@kadrlica)](https://github.com/kadrlica)
* Heather Kelly [(@heather999)](https://github.com/heather999)
* Jonathan Sick [(@jonathansick)](https://github.com/jonathansick)

This is open source software, available under the BSD license. If you are interested in this project, please do drop us a line via the hyperlinked contact names above, or by [writing us an issue](https://github.com/DarkEnergyScienceCollaboration/start_paper/issues).
