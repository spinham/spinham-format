.DEFAULT_GOAL := help

# Sphinx-related variables
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = _build

help:
	@echo "\x1b[31m"
	@echo "Please specify what do you want to do."
	@echo "\x1b[0m"
	@echo "Available options are:\n"
	@echo "    help - show this message"
	@echo "    html - build the html docs"
	@echo "    clean - clean all files from docs and pip routines"
	@echo "    clean-html - clean all files from docs and build html docs from scratch"

clean:
	-@rm -r docs/_build

html:
	@$(SPHINXBUILD) -M html "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS)


clean-html: clean html
	@echo "Done"

