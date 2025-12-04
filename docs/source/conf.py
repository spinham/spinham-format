import sys
from os.path import abspath, join
from pathlib import Path

sys.path.insert(0, abspath(join("..", "..")))
sys.path.append(str(Path("_ext").resolve()))


##########################################################################################
##                                   Project metadata                                   ##
##########################################################################################
project = "spinham-format"


##########################################################################################
##                                      Extensions                                      ##
##########################################################################################
extensions = [
    "sphinx.ext.duration",  # Measure the time of the build
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.extlinks",  # Markup to shorten external links
    "sphinx.ext.mathjax",  # For latex-style math
    "sphinx_copybutton",  # Copybutton for the blocks
]


##########################################################################################
##                                  Build configuration                                 ##
##########################################################################################
smartquotes = False

##########################################################################################
##                                Options for HTML output                               ##
##########################################################################################

htmlhelp_basename = "spinham-format"
html_theme = "furo"
html_title = "Spinham format"
# html_static_path = ["_static"]

html_context = {
    "default_mode": "light",
    "display_github": True,  # Integrate GitHub
    "github_user": "spinham",  # Username
    "github_repo": "spinham-format",  # Repo name
    "github_version": "main",
    "doc_path": "docs/source",  # Path in the checkout to the docs root
}


##########################################################################################
##              Custom variables with access from .rst files and docstrings             ##
##########################################################################################

# Custom variables with access from .rst files and docstrings
variables_to_export = ["project"]

frozen_locals = dict(locals())
rst_epilog = "\n".join(
    map(lambda x: f".. |{x}| replace:: {frozen_locals[x]}", variables_to_export)  # noqa F821
)
del frozen_locals

# Dynamic external links
# Usage :issue:`123`
extlinks = {
    "DOI": ("https://doi.org/%s", "DOI: %s"),
    "issue": ("https://github.com/spinham/spinham-format/issues/%s", "issue #%s"),
}

# Static external links
# Solution source:
# https://docutils.sourceforge.io/docs/ref/rst/directives.html#directives-for-substitution-definitions
# Usage: |Python|_
custom_links = {
    "reStructuredText": (
        "reStructuredText",
        "https://docutils.sourceforge.io/rst.html",
    ),
    "spinham-format": (
        "spinham-format",
        "https://github.com/spinham/spinham-format",
    ),
    "issues": ("issues", "https://github.com/spinham/spinham-format/issues"),
}
rst_epilog += "\n".join(
    map(
        lambda x: f"\n.. |{x}| replace:: {custom_links[x][0]}\n.. _{x}: {custom_links[x][1]}",
        [i for i in custom_links],
    )
)
