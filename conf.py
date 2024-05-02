# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AnnotationBot'
copyright = '2024, Morozov I.M. Kononenko S.S. Bokov A.D.'
author = 'Morozov I.M. Kononenko S.S. Bokov A.D.'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'Python'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_title = 'Documentation for AnnotationBot'
version = '1.0'

language = 'en'
html_theme = 'sphinx_rtd_theme'

source_suffix = ['.rst']
master_doc = 'index'

