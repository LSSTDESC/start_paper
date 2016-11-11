# To make the document with the default settings:
# > make
#
# To make with a specific format:
# > make <format>
#
# To tar up a flat version of a specific format:
# > make <format> tar

# Primary file names
main=main
filename=${ {{ cookiecutter.folder_name }} }

# LATEX environment variables
export TEXINPUTS:=.:./texmf//:./tex:./tex/texmf//:
export BSTINPUTS:=.:./texmf/bib/:./tex:./tex/texmf/bib/:

# Document class switcher flags
aastex=\def\flag{aastex}
revtex=\def\flag{revtex}

# Submission flags
arxiv=\def\flag{emulateapj}
submit=${aastex}
#draft=${aastex}\def\linenums{\linenumbers}
draft=${aastex}

# Files to copy when making tarball
tardir=tmp
figdir=../figs
figures=
source=$(filename)_apjl.tex 

tarfiles=$(figures) $(source)

all: export flag = ${draft}
all: main copy

copy: 
	cp $(filename).pdf $(out).pdf

touch:
	touch ${filename}.tex

# http://stackoverflow.com/q/8028314/
TARGETS=aastex note
$(TARGETS): export flag = \def\flag{$(@)}
$(TARGETS): 
	$(MAKE) -e main
	$(MAKE) -e tar

main : 
	pdflatex "${flag}\input{${main}}"
	bibtex ${filename}||true
	pdflatex "${flag}\input{${main}}"
	pdflatex "${flag}\input{${main}}"

tar : main
	mkdir -p $(tardir)
	cp $(tarfiles) $(tardir)	
	cp $(filename).pdf $(tardir)/$(out).pdf
	cd $(tardir) && tar -czf ../$(out).tar.gz . && cd ..
	rm -rf $(tardir)

clean:
	rm -f *.ps ${filename}.pdf *.log *.aux *.out *.dvi *.bbl *.blg *Notes.bib *.synctex.gz *.fdb_latexmk *.fls

