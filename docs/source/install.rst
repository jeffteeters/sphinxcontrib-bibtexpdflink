.. _installation:

Installation
============

Install the extension with:

.. code-block:: shell

    $ pip install --index-url https://test.pypi.org/simple/ sphinxcontrib-bibtexpdflink

(This installs from Test PyPI).


The package is not yet on the real PyPI, but when it is, the installation command will be:


.. code-block:: shell

    $ pip install sphinxcontrib-bibtexpdflink


Configuring
-----------

Add the extension to the Sphinx ``conf.py`` file (along with sphinxcontrib.bibtex and sphinxcontrib.bibtex2 extensions):

.. code-block:: shell

    extensions = [
        "sphinxcontrib.bibtex",
        "sphinxcontrib.bibtex2",
        "sphinxcontrib.bibtexpdflink",
        ]


In the ``conf.py`` file, specify the directories for PDF and notes files using config variables *bibtexpdflink_note_dir*
and *bibtexpdflink_pdf_dir*.  An example is:

.. code-block:: shell

    bibtexpdflink_note_dir = "notes"
    bibtexpdflink_pdf_dir = "papers"


The directory specified for *bibtexpdflink_pdf_dir* must be inside the directory specified for
html_static_path[0].  For example, if

.. code-block:: shell

    html_static_path = ['_static']

and

.. code-block:: shell

    bibtexpdflink_pdf_dir = "papers"

Then the pdf files must be placed in directory: ``_static/papers``.


The names of the pdf and notes files must be the same as the bibtex citation key, but respectively 
with extension ".pdf" and ".rst". 
