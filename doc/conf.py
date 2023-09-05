"""Sphinx configuration."""
import datetime

import pkg_resources

# Sphinx configuration below.
project = "amazon-braket-sdk"
version = pkg_resources.require(project)[0].version
release = version
copyright = "{}, Amazon.com".format(datetime.datetime.now().year)

extensions = [
    "sphinxcontrib.apidoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "jupyterlite_sphinx",
    'sphinx_design'
    # 'nbsphinx',
    # 'myst_parser'
]

source_suffix = ".rst"
master_doc = "index"

autoclass_content = "both"
autodoc_member_order = "bysource"
default_role = "py:obj"

html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
html_logo = "_static/amz-braket.png"
html_title = "Amazon Braket Python SDK"
htmlhelp_basename = "{}doc".format(project)

html_theme_options = {
    "repository_url": "https://github.com/executablebooks/sphinx-design",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "repository_branch": "main",
    "path_to_docs": "doc",
    "home_page_in_toc": False,
}

language = "en"

napoleon_use_rtype = False

apidoc_module_dir = "../src/braket"
apidoc_output_dir = "_apidoc"
apidoc_excluded_paths = ["../test"]
apidoc_separate_modules = True
apidoc_module_first = True
apidoc_extra_args = ["-f", "--implicit-namespaces", "-H", "API Reference"]

# jupyterlite_bind_ipynb_suffix = False
jupyterlite_contents = "./jupyter_contents"