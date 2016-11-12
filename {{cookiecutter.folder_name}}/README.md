
## {{ cookiecutter.folder_name }}
# {{ cookiecutter.title }}

* {{ cookiecutter.authors }} *

{{ cookiecutter.description }}


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
make  [note|apj|apjl|prd|prl|mnras]
```

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
