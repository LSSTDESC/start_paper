
## desc-0000-start_paper-intro
# How to Start Writing an LSST DESC Paper

* Phil Marshall, Alex Drlica-Wagner, Heather Kelly, Jonathan Sick *

A short paper describing the "start_paper" project, including the cookiecutter mechanism and the various templates.

## Editing this Paper

Fork and/or clone the project repo, and then
edit the primary file. The name of this file will vary according to its format, but it should be one of either `main.rst` (if it's a [`reStructuredText`](http://docutils.sourceforge.net/rst.html) Note), `main.md` (if it's a [`Markdown`](https://github.com/adam-p/Markdown-here/wiki/Markdown-Cheatsheet) Note), `main.ipynb` (if it's an [`IPython Notebook`](https://ipython.org/notebook.html)) or `main.tex` (if it's a latex Note or paper).
Please use the `figures` folder for your images.

## Building this Paper

GitHub is our primary distributor for LSST DESC Notes:
once the Note has been merged into the project repo's master branch, it will be visible as a *shared* (but not *published*) paper. The presentation of Notes will be improved later, as the LSST DESC Publication System evolves.

Automatically building latex-format Notes or journal articles into PDF files is not yet supported but hopefully will be soon.
You can compile latex papers locally with
```
make  [apj|apjl|prd|prl|mnras]
```
(`make` with no arguments compiles latex in LSST DESC Note style.)

From time to time, the latex style files will be updated: to re-download the latest versions, do
```
make update
```
This will over-write your folder's copies - but that's OK, as they are not meant to be edited by you!
The template files (`main.*` etc) are also likely to be updated; to get fresh copies of these files, do
```
make templates
```
However, since you will have edited at least one of the templates in your folder, `make templates` creates a special `templates` folder for you to refer to. Finally, to get *new* style or template files that are added to the `start_paper` project, you'll need to first get the latest `Makefile`, and then `make update` and/or `make templates`. The command to obtain the latest `Makefile` is
```
make new
```
This will add the latest `Makefile` to your `templates` folder. If you want to over-write your existing `Makefile`, you can do
```
make upgrade
```

## Automatic PDF Sharing

The `.travis.yml` file in this folder will cause [travis-ci](http://travis-ci.org) to compile your paper into a PDF in the base repo at GitHub every time you push a commit. The paper should appear as:

**https://github.com/DarkEnergyScienceCollaboration/start_paper/tree/pdfdesc-0000-start_paper-intro.pdf**

To enable this service, you need to follow these steps:

1. Turn on travis continuous integration, by [toggling your repo on your travis profile](https://travis-ci.org/profile). If you don't see your repo listed, you may not have permission to do this: in this case, [contact an admin via the issues](https://github.com/DarkEnergyScienceCollaboration/start_paper/issues/new?body=@DarkEnergyScienceCollaboration/admin).
2. Get a [GitHub "personal access token"](https://github.com/settings/tokens). Choose the "repo" option.
3. Set the `GITHUB_API_KEY` environment variable with the value of this token at your repo's [travis settings page](https://travis-ci.org/DarkEnergyScienceCollaboration/start_paper/settings).
4. Copy the `.travis.yml` file in this folder to the top level of your repo (or merge its contents with your existing `.travis.yml` file).
Edit the final `git push` command with your GitHub username.  
Commit and push to trigger your travis PDF build.
