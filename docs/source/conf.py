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

project = 'Eufloria RPG Modding'
copyright = '2020, Omni Systems'
author = 'Omni Systems'

# The full version, including alpha/beta/rc tags
release = '0.0.6a'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# YOU NEED ONE OF THE FOLLOWING SETS OF EXTENSIONS ENABLED AT A TIME, PLEASE SEE
# THE COMMENT ABOVE EACH ONE TO SEE WHAT YOU DO / DO NOT NEED ENABLED BASED ON YOUR REQUIREENTS

# WHEN YOU WANT TO GENERATE THE API DOCUMENTATION, UNCOMMENT THE FOLLOWING
#extensions = [
#    'sphinxcontrib.dotnetdomain',
#    'sphinx.ext.autodoc', 
#    'autoapi.extension',
#    "sphinx_rtd_theme",
#]
# WHEN YOU DON'T WANT TO REGENERATE THE API DOCUMENTATION UNCOMMENT THE FOLLOWING
extensions = [
    'sphinxcontrib.dotnetdomain',
    'sphinx.ext.autodoc',
    "sphinx_rtd_theme"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']





# Settings for sphinx autoapi
autoapi_type = 'dotnet'
autodoc_typehints = 'description'

# Keep our generated API files, when we have finished generating the api files, we turn off generation and commit the generated
# files to our repository, this allows us to build our documentation seperately from the api documentation through readthedocs
autoapi_keep_files = True
autoapi_generate_api_docs = False

# The path we look for the dockfx.json file in
autoapi_dirs = [
    '../',
]

# Configuration options for what to generate with autoapi, see below for a the DEFAULT list of options
autoapi_options = [
    'members',
    'show-inheritance', 
    'show-module-summary', 
    'special-members', 
    'imported-members'
]


# Default autoapi_options, for reference
#autoapi_options = [
#    'members',
#    'undoc-members', 
#    'private-members', 
#    'show-inheritance', 
#    'show-module-summary', 
#    'special-members', 
#    'imported-members'
#]