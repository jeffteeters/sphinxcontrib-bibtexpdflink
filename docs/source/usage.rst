Usage
=====

Name the PDF files and notes files as described in :ref:`installation`.


Use the normal bibtex or bibtex2 directives:

.. code-block:: rst

   See :cite:`JaeckelLA-1989a` also :footcite:`JaeckelLA-1989a` for more details.

   Some random text...

   .. footbibliography::



This will be rendered as:

See :cite:`JaeckelLA-1989a` also :footcite:`JaeckelLA-1989a` for more details.

Some random text...

.. footbibliography::


Generating a list of the notes
------------------------------


To generate a list of notes files, put an additional ".rst" file in the directory containing
the notes (the name of the file could be "notes.rst").
Include in the file a ``toctree::`` directive like in the following:

.. code-block:: rst

   The following notes are available:
   
   .. toctree::
      :glob:
   
      *


This will be rendered as shown on the :ref:`notes` page.


