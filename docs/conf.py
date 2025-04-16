#!/usr/bin/env python3
#
# pint documentation build configuration file, created by
# sphinx-quickstart on Thu Mar  1 13:33:14 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
from __future__ import annotations

import datetime
from importlib.metadata import version

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "matplotlib.sphinxext.plot_directive",
    "nbsphinx",
    "sphinx_copybutton",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx_design",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "pint"
author = "Hernan E. Grecco"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

try:  # pragma: no cover
    version = version(project)
except Exception:  # pragma: no cover
    # we seem to have a local copy not installed without setuptools
    # so the reported version will be unknown
    version = "unknown"

release = version
this_year = datetime.date.today().year
copyright = f"2012-{this_year}, Pint Developers"

exclude_patterns = ["_build"]

# Napoleon configurations

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_preprocess_types = True
napoleon_type_aliases = {
    # general terms
    "sequence": ":term:`sequence`",
    "iterable": ":term:`iterable`",
    "callable": ":py:func:`callable`",
    "dict_like": ":term:`dict-like <mapping>`",
    "path-like": ":term:`path-like <path-like object>`",
    "mapping": ":term:`mapping`",
    "file-like": ":term:`file-like <file-like object>`",
    # stdlib type aliases
    "timedelta": "~datetime.timedelta",
    "datetime": "~datetime.datetime",
    "string": ":class:`string <str>`",
    "Path": "~pathlib.Path",
    # numpy terms
    "array_like": ":term:`array_like`",
    "array-like": ":term:`array-like <array_like>`",
    "scalar": ":term:`scalar`",
    "array": ":term:`array`",
    "hashable": ":term:`hashable <name>`",
    # objects without namespace: pint
    "Quantity": "~pint.Quantity",
    "Unit": "~pint.Unit",
    "UnitsContainer": "~pint.UnitsContainer",
    # objects without namespace: numpy
    "ndarray": "~numpy.ndarray",
    "MaskedArray": "~numpy.ma.MaskedArray",
    "dtype": "~numpy.dtype",
}


html_theme = "sphinx_book_theme"

html_theme_options = {
    "repository_url": "https://github.com/hgrecco/pint",
    "repository_branch": "master",
    "use_repository_button": True,
    "use_issues_button": True,
    "extra_navbar": "",
    "navbar_footer_text": "",
}

html_logo = "_static/logo-full.jpg"

html_static_path = ["_static"]
html_css_files = ["style.css"]

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}
# html_sidebars = {
#     "index": ["sidebarintro.html", "sourcelink.html", "searchbox.html"],
#     "**": [
#         "sidebarlogo.html",
#         "localtoc.html",
#         "relations.html",
#         "sourcelink.html",
#         "searchbox.html",
#     ],
# }

# Output file base name for HTML help builder.
htmlhelp_basename = "pintdoc"


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    "preamble": "".join((r"\DeclareUnicodeCharacter{2212}{-}",))  # MINUS
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ("index", "pint.tex", "pint Documentation", "Hernan E. Grecco", "manual")
]


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "pint", "pint Documentation", ["Hernan E. Grecco"], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "pint",
        "pint Documentation",
        "Hernan E. Grecco",
        "pint",
        "One line description of project.",
        "Miscellaneous",
    )
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "dask": ("https://docs.dask.org/en/latest", None),
    "sparse": ("https://sparse.pydata.org/en/latest/", None),
}

# -- Doctest configuration -----------------------------------------------------

# fill a dictionary with package names that may be missing
# this is checked by :skipif: clauses in certain doctests that rely
# on optional dependencies
doctest_global_setup = """
from importlib.util import find_spec

not_installed = {
    pkg_name: find_spec(pkg_name) is None
    for pkg_name in [
        'uncertainties',
        'serialize',
    ]
}
"""
