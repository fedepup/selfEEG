# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, '..')


# -- Project information -----------------------------------------------------

project = 'SelfEEG'
copyright = '2023, MedMax Team'
author = 'MedMax Team'


# The short X.Y version
version = '0.1.0'
# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    #'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'nbsphinx',
    'myst_parser',
    'sphinx_automodapi.automodapi',
    #'sphinx.ext.doctest'
]
#doctest_test_doctest_blocks = 'default'
#doctest_global_setup = '''
#try:
#    import matplotlib.pyplot as plt
#except ImportError:
#    plt = None
#'''
numpydoc_show_class_members = False
autodoc_type_aliases = {
    'Iterable': 'Iterable',
    'ArrayLike': 'ArrayLike',
}
autodoc_default_options = {
    "private-members": True,
}
napoleon_custom_sections = [('Returns', 'params_style')]

source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
#html_logo = '_static/LibraryLogo.png'

# html rtd theme configuration parameters
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': False,
    #'sticky_navigation': True,
    #'style_nav_header_background': '#E3E3E3',
    'navigation_depth': -1,
    'includehidden': False,
    'titles_only': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
