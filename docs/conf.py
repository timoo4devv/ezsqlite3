# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import datetime

project = "ezsqlite3"
copyright = f"{datetime.date.today().year}, Timo Schneider"
author = "Timo Schneider"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_mdinclude",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

autodoc_default_options = {
    "show-inheritance": True,
    "members": True,
    "undoc-members": True,
}
autodoc_member_order = "groupwise"
autodoc_typehints = "description"

highlight_language = "text"
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
html_theme_options = {
    "description": "Sqlite for Python AsyncIO",
    "fixed_sidebar": True,
    "badge_branch": "master",
    "github_button": False,
    "github_user": "timoo4devv",
    "github_repo": "ezsqlite3",
    "show_powered_by": False,
    "sidebar_collapse": False,
    "extra_nav_links": {
        "Report Issues": "https://github.com/timoo4devv/ezsqlite3/issues",
    },
}

html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
    ],
}