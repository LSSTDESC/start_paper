# start_paper

Use Cookiecutter to make a folder containing everything you need to start writing an LSST DESC paper (either a journal article or a Note). This follows Jonathan Sick's [`lsst_technote_bootstrap`](https://github.com/lsst-sqre/lsst-technote-bootstrap) method, albeit with a simpler set-up.

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
This will ask you for a serial number, and then make a suitably-named folder containing template files etc for you. You'll need to git add and commit from there, in the usual way.

For LSST DESC Notes, you have a range of format choices available to you: Markdown, rST, ipynb and latex. The templates are in the templates folder. For journal papers, we provide the AJ style files for convenience, as well as some useful macros.

## Licence, credits etc

People developing this project:
* Phil Marshall [(@drphilmarshall)](https://github.com/DarkEnergyScienceCollaboration/start_paper/issues/new?body=@drphilmarshall)

This is open source software, available under the BSD license. If you are interested in this project, please do drop us a line via the hyperlinked contact names above, or by [writing us an issue](https://github.com/DarkEnergyScienceCollaboration/start_paper/issues?q=).
