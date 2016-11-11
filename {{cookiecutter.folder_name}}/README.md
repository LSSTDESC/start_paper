
## {{ cookiecutter.folder_name }}
# {{ cookiecutter.title }}

* {{ cookiecutter.authors }} *

{{ cookiecutter.description }}


## Editing this Paper

Fork and/or clone the project repo, and then
edit the primary file. The name of this file will vary according to its format, but it should be one of either `main.rst` (if it's a reStructuredText Note), `main.md` (if it's a Markdown Note), `main.ipynb` (if it's a jupyter notebook Note) or `main.tex` (if it's a latex Note or paper).

Please use the `figures` folder for your images.

## Building this Paper

GitHub is our primary distributor for LSST DESC Notes in `rST`, `Markdown` or `ipynb` formats: once the Note has been merged into the project repo's master branch, it will be visible as a *shared* (but not *published*) paper. The presentation of Notes will be improved later, as the LSST DESC Publication System evolves.

Automatically building latex-format Notes or journal articles into PDF files is not yet supported but hopefully will be soon.
You can compile latex papers locally with
```
make  [note|apj|apjl|prd|prl|mnras]
```
