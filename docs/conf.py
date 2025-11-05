# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'durham'
copyright = '2024-2025, Durham'
author = 'durham'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinx.ext.githubpages",
    "sphinx_rtd_theme",
    'myst_parser',
]

myst_enable_extensions = ['attrs_inline']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# List of source directory to ignore 
exclude_patterns = [
    'cpu/sapphire-rapids.md'
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = 'images/logo.png'
html_favicon = 'images/durham.ico'
html_theme_options = {
    'logo_only': True
}

# Show the edit this file.  Didn't work.
#html_show_sourcelink = True

html_context = {
    'display_github': True,
    'github_user': 'agb32',
    'github_repo': 'durham',
    'github_version': 'main/docs/',
#    'conf_py_path': '/source/', 
}


# -- Options for EPUB output
epub_show_urls = 'footnote'
