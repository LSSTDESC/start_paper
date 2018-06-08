
# start_paper
### Jump-start your DESC paper or note

`start_paper` is intended to make the process of starting to write a DESC paper or note, and later transforming notes into papers, as simple as possible. `start_paper` attempts to play well with [`desc-tex`](https://github.com/LSSTDESC/desc-tex), a repository of latex support files for DESC papers, and [`mkauthlist`](https://github.com/kadrlica/mkauthlist), a Python package for generating author and contribution lists in latex format.

Please submit issues or feature requests to the [issues](https://github.com/LSSTDESC/start_paper/issues). However, please also note that `start_paper` and `desc-tex` are now separate projects, and that `desc-tex` related items (including anything to do with the DESC Note class) belong in the [`desc-tex` issues](https://github.com/LSSTDESC/desc-tex/issues). Thank you.

## Starting your paper

Download the contents of the [`deploy` branch](https://github.com/LSSTDESC/start_paper/tree/deploy) of the `start_paper` repository. We recommend downloading it as a ZIP file rather than cloning the repository; this simplifies the process of versioning your paper in its own repository, if you so desire. You can either do this manually by clicking "Clone or download" and then "Download ZIP" in GitHub (*while looking at the [`deploy` branch](https://github.com/LSSTDESC/start_paper/tree/deploy)*), or automatically by [downloading](https://raw.githubusercontent.com/LSSTDESC/start_paper/master/deploy_from_github_zip.bash) and running [this BASH script](https://github.com/LSSTDESC/start_paper/blob/master/deploy_from_github_zip.bash), as in

```bash
wget https://raw.githubusercontent.com/LSSTDESC/start_paper/master/deploy_from_github_zip.bash
bash ./deploy_from_github_zip.bash MyNewPaper
```

This will download and unzip the `start_paper` files to a new folder called `MyNewPaper/`.

`start_paper` provides templates in various formats: [Jupyter Notebook](https://ipython.org/notebook.html) (`main.ipynb`), [Markdown](https://github.com/adam-p/Markdown-here/wiki/Markdown-Cheatsheet) (`main.md`), [reStructuredText](http://docutils.sourceforge.net/rst.html) (`main.rst`), and [LaTeX](http://www.latex-project.org/) (`main.tex`). There is also a template [Google Doc](https://docs.google.com/document/d/1ERz_S02Uvc0QkapVx145PrYZT0CRJbkPMmY5T95uMkk/edit?usp=sharing) than lives in the cloud.

For tips on writing papers in each of these formats, see the corresponding `example.*` files in this repository (note that these are not included in the downloaded files) or [here](https://docs.google.com/document/d/1WaGmnG67Ziajo6fBD3Y9HR4YkN2itMmzA549i-sbCc8/edit?usp=sharing) in the case of the Google Doc format.

## Building your paper

At present, only latex documents require/benefit from the Makefile. `make` or `make help` will display basic options; more detailed documentation on using the Makefile and on writing papers/notes in latex and other formats will be provided in another document (started, appropriately enough, with `start_paper`).


## Updating `start_paper` content

From time to time, there may be updates to the latex support files provided by [`desc-tex`](https://github.com/LSSTDESC/desc-tex), or the `start_paper` templates or Makefile.

```
make templates
```
will download the latest templates and Makefile to a `templates/` directory (i.e., not directly over-writing any files in the main directory).

```
make update
```
will do the same, and will also attempt to update [`desc-tex`](https://github.com/LSSTDESC/desc-tex) and [`mkauthlist`](https://github.com/kadrlica/mkauthlist).

## Everything breaks because I can't install `mkauthlist`!

Try passing `make` the `localpip=T` flag, as in `make localpip=T main`. This will download and run `mkauthlist` in the current working directory instead of trying to install it. The default value of `localpip` can be changed in `Makefile`; look for the line `localpip ?= F`.

## Using Overleaf

[Overleaf](https://www.overleaf.com/) is an online collaborative writing and publishing tool using LaTeX. It allows you to interactively edit latex documents using your browser. Under the hood, Overleaf is just a wrapper around a git repository, which can be directly cloned and editted if you desire. To use `start_paper` in Overleaf:

* Follow the [instructions above](#starting-your-paper) to deploy your new paper.
* Follow [these instructions](https://github.com/LSSTDESC/desc-tex/blob/master/README.md#standalone-deployment) to install a standalone version of [`desc-tex`](https://github.com/LSSTDESC/desc-tex) (Overleaf does not allow submodules).
* Follow [these instructions](http://kbroman.org/github_tutorial/pages/init.html) to initialize a git repo for your paper.
* Follow [these instructions](https://www.overleaf.com/help/230-how-do-i-push-a-new-project-to-overleaf-via-git) to push your project to a new Overleaf directory. (Note: you will probably want to use `git pull -s ours` to resolve conflicts in `main.tex`.)
* Write on Overleaf!

The code below shows how to do this (you will of course need to change the names "doc" and "4551529zqsdhy" appropriately).

```
# Deploy the start_paper template into a directory called "doc"
wget https://raw.githubusercontent.com/LSSTDESC/start_paper/master/deploy_from_github_zip.bash
bash ./deploy_from_github_zip.bash doc

# Deploy desc-tex into "doc"
bash ./deploy_from_github_zip.bash doc/desc-tex LSSTDESC/desc-tex master

cd doc

# Initialize the repo
git init
git add .
git commit -m "init repo"

# Follow the overleaf instructions to create a new project
# Add your new overleaf repo as a remote 
# (be sure to use the link to your new repo, not the example below)
git remote add overleaf https://git.overleaf.com/4551529zqsdhy

# Grab from overleaf
git checkout master
git pull overleaf master --allow-unrelated-histories -s ours

# Ignore overleaf changes
git revert --mainline 1 HEAD

# Push back to overleaf
git push overleaf master
```

## Converting non-latex formats to PDF

At present, the facilities exist to convert these formats to PDF, though not with a layout consistent with compiled latex DESC Notes (e.g. with images and captions placed exactly rather than "floated" to the top of the page). Most require [Pandoc](http://pandoc.org/).

* Jupyter notebook:
* Markdown:
* reStructuredText:
* Google Doc: Export from Google Docs using File... Download as... Web Page (.html, zipped). Convert from HTML to PDF with Pandoc.

## Detailed `make` usage

`make` or `make help` will display the possible `make` targets, of which there are many. Lots of defaults, such as the "main" naming for targets and the default latex style, can be changed in `Makefile`.

`make main` tries to compile `main.tex` into `main.pdf`. `main.tex` internally depends on `main.bib`, where you should put your own `bibtex` entries, `authors.tex`, and `contributions.tex`.

You can manually enter the appropriate `\author` command(s) in `authors.tex`, and text in `contributions.tex`. Alternatively, these two files can be generated automatically using `mkauthlist`, based on information in `authors.csv`. `make` will attempt to do this automatically when compiling if `authors.csv` is newer (modified more recently) than `authors.tex`. Specifically, it will try to
1. download and install `mkauthlist`, and
2. run `mkauthlist`, overwriting `authors.tex` and `contributions.tex`.

The first step can cause problems if you do not have write access to your system-wide Python library files. See "Everything breaks because I can't install `mkauthlist`!" above.

By default, latex will compile using the LSST-DESC Note class. To use another class, pass the `style` argument to `make`, as in `make style=apj main`. Note that the output of `mkauthlist` depends on the journal style, so you should delete `authors.tex` when changing style to avoid incompatibilities. For convenience, you could also change the default style in the `Makefile`; look for the line `style ?= lsstdescnote`.

There's more - write us issues if you find that the `make` options are insufficiently explained by `make help`, or if you encounter other problems.

## Contributors to `start_paper`

People developing this project:
* Phil Marshall [(@drphilmarshall)](https://github.com/drphilmarshall)
* Alex Drlica-Wagner [(@kadrlica)](https://github.com/kadrlica)
* Adam Mantz [(@abmantz)](https://github.com/abmantz)
* Heather Kelly [(@heather999)](https://github.com/heather999)
* Jonathan Sick [(@jonathansick)](https://github.com/jonathansick)

This is open source software, available under the BSD license. If you are interested in this project, please do drop us a line via the hyperlinked contact names above, or by [writing us an issue](https://github.com/DarkEnergyScienceCollaboration/start_paper/issues).
