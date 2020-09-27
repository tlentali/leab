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
import os
import sys
import recommonmark
from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'le AB'
copyright = '2020, tlentali'
author = 'tlentali'

# The full version, including alpha/beta/rc tags
release = '0.1.4'

autodoc_mock_imports = ['tkinter']
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['m2r',
              'sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'sphinx.ext.viewcode',
              'sphinx_copybutton',
              'sphinxemoji.sphinxemoji']


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
#html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


import matplotlib
matplotlib.use('agg')


import sphinx_material

 # Register the theme as an extension to generate a sitemap.xml
extensions.append('sphinx_material')

# Choose the material theme
html_theme = 'sphinx_material'
# Get the them path
html_theme_path = sphinx_material.html_theme_path()
# Register the required helpers for the html context
html_context = sphinx_material.get_html_context()


html_show_sourcelink = True
html_sidebars = {
    '**': ['logo-text.html', 'globaltoc.html', 'localtoc.html', 'searchbox.html']
}
html_static_path = ['_static']
html_use_index = True
html_domain_indices = True
html_favicon = '_static/target.ico'
html_logo = '_static/target.png'

html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': f'le AB v{release}',

    # Set you GA account ID to enable tracking
    'google_analytics_account': 'UA-34150465-7',

    # Set the color and the accent color
    #'color_primary': 'white',
    #'color_accent': 'red',

    'nav_links': [],

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/tlentali/leab/',
    'repo_name': 'leab',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 1,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True
}

# nbsphinx

extensions.append('nbsphinx')
nbsphinx_execute = 'never'


#exclude_patterns = ['pages/reference-architecture', some/other/file.txt]

# napolean

extensions.append('sphinx.ext.napoleon')
napoleon_use_rtype = False
napoleon_use_ivar = True

# autosummary

extensions.append('sphinx.ext.autosummary')
autoclass_content = 'class'
autosummary_generate = True
autosummary_generate_overwrite = False
autodoc_default_options = {
    'show-inheritance': True
}
