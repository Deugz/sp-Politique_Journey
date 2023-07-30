# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Encyclopedia 3.A'
copyright = '2023, Vincent Deguin'
author = 'Vincent Deguin'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

comments_config = {
   "utterances": {
      "repo": "https://github.com/Deugz/Encyclopedia-Home",
      "optional": "config",
   }
}

comments_config = {
   "hypothesis": True
}



extensions = [
  
  "myst_parser",
  "sphinx_design",
  "sphinx_comments",
  "sphinx_new_tab_link",
  "sphinx_book_theme",
  "sphinx_togglebutton",
  "sphinx_thebe",
]

myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_heading_anchors = 2



templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/Logo/Encyclopedia-logo.png"
html_favicon = "_static/Logo/Encyclopedia-logo.png"
html_static_path = ['_static']

html_theme_options = {
    "external_links": [
        {
            "url": "https://deugz.github.io/nb-sbfp/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp 💫 Science",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/nb-notes/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp 🧠 Education",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/nb-publi/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp 🎤 Music ",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/nb-teaching/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp 💊 Pharmacie",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/nb-blog/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp ✊ Politique",
            "attributes": {"target": "_blank"},
        },
    ],
    "header_links_before_dropdown": 10,    
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Deugz/Encyclopedia-Home",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Home",
            "url": "https://deugz.github.io/Encyclopedia-Home/build/html/index.html",
            "icon": "fa-solid fa-house",
        },
        {
            "name": "Profile",
            "url": "https://deugz.github.io/nb-profile/_build/html/intro.html",
            "icon": "fa-solid fa-user",
        },
        {
            "name": "Blog",
            "url": "https://deugz.github.io/ab-blog/_website/index.html",
            "icon": "fa-solid fa-blog",
        },
        {
            "name": "Tools",
            "url": "https://deugz.github.io/nb-tools/_build/html/intro.html",
            "icon": "fa-solid fa-screwdriver-wrench",
        },
    ],
    

    "logo": {
        "text": " &nbsp V. Deguin &nbsp ",
        "image_dark": "_static/Logo/logo_SFTP.png",
        "alt_text": " &nbsp V. Deguin &nbsp &nbsp",
    },
    
    
    "navbar_start": ["navbar-logo"],
    
}


html_css_files = ["css/custom_style.css", "css/Cube.css", "css/coffee_cup.css", "css/kittons.css", "css/style_book_shell.css", "css/style_flipping_card.css", "css/style_wheel.css"]
html_js_files = ["assets/script/kittons.js", "assets/script/script_flipping_card.js", "assets/script/script_wheel.js", "assets/script/scriptvideo.js", "assets/script/slideshow.js"]

    
