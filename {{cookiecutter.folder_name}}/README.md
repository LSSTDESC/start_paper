
## {{ cookiecutter.folder_name }}
# {{ cookiecutter.title }}

{{ cookiecutter.description }}

Authors:
* {{ cookiecutter.first_author }}

## Editing this Paper

Fork and/or clone the project repo, and then
edit the primary file. The name of this file will vary according to its format, but it should be one of either `index.rst` (if it's a reStructuredText Note), `index.md` (if it's a Markdown Note), `index.ipynb` (if it's a jupyter notebook Note) or `main.tex` (if it's a latex Note or paper).

For the non-latex formats, please use the `_static` folder for your images. For latex, you can go ahead and make sub-folders for figures as usual.

## Building this Paper

GitHub is our primary publisher for LSST DESC Notes in rST, Md or ipynb formats: once the Note has been merged into the project repo's master branch, it will be visible as a "published" paper. This presentation may be improved later, as the LSST DESC Publication System evolves.

Automatically building latex-format Notes or journal articles into PDF files is not yet supported but hopefully will be soon.
You can compile latex papers locally with
```
make
```
