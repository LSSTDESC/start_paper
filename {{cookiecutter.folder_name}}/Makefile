# To make the document with the default settings:
# > make
#
# To make with a specific format:
# > make <format>
#
# To tar up a flat version of a specific format:
# > make <format> tar
#
# Alex Drlica-Wagner <kadrlica@fnal.gov>
#

# Primary file names
main=main
#filename={{ cookiecutter.folder_name }}
outname=paper

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
figdir=./figures
figures=$(figdir)/*.pdf
tabdir=./tables
tables=$(tabdir)/*.tex
stydir=./texmf
styles=$(stydir)/styles/*.{sty,cls}
source=$(main).{tex,bbl,bib} macros.tex authors.tex acknowledgments.tex

tarfiles=$(figures) $(tables) $(styles) $(source)

all: export flag = ${draft}
all: main copy

copy: 
	cp ${main}.pdf ${outname}.pdf

touch:
	touch ${main}.tex

# http://stackoverflow.com/q/8028314/
TARGETS=aastex note
$(TARGETS): export flag = \def\flag{$(@)}
$(TARGETS): 
	$(MAKE) -e authlist
	$(MAKE) -e main
	$(MAKE) -e tar

main : 
	# {% raw %}
	latexmk -pdf  \
	-pdflatex='pdflatex %O -interaction=nonstopmode "${flag}\input{%S}"'  \
	${main}
	# {% endraw %}

tar : main
	mkdir -p ${tardir}
	cp ${tarfiles} ${tardir}
	cp ${main}.pdf ${tardir}/${outname}.pdf
	cd ${tardir} && tar -czf ../${outname}.tar.gz . && cd ..
	rm -rf ${tardir}

clean:
	rm -f *.log *.aux *.out *.dvi *.synctex.gz *.fdb_latexmk *.fls
	rm -f *.bbl *.blg *Notes.bib
	rm -f ${main}.pdf ${main}.tar.gz

