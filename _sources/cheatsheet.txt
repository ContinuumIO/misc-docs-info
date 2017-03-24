============================
reStructuredText cheat sheet
============================

.. contents::
   :local:

This cheat sheet explains how to use common reStructuredText formatting with the Sphinx documentation generator.

Headings
========

Start each section in a page with a heading. Use H1 for the page's title, H2 for the page's sections and H3 for the subsections.

.. code-block:: rst

    ==========
    Header One
    ==========

    Header Two
    ==========

    Header Three
    ------------

    Header Four
    ^^^^^^^^^^^

    Header Five
    """""""""""

NOTE: The lines below and above a header must be at least the length of the text.

NOTE: H4 and H5 are discouraged and rarely used.

NOTE: Sphinx will actually accept any header style it encounters first as H1, the next as H2, and so on, but we prefer to use these styles for consistency.

Tables of contents
==================

We use two types of tables of contents (TOCs):

#. TOCTREE: This organizes the pages and creates a nested list of links to each page in the left navigation.
#. CONTENTS: This creates a nested list of links to sections of the current page as in-page navigation.

Sphinx keeps pages in a `tree data structure <https://en.wikipedia.org/wiki/Tree_(data_structure)>`_ where each node is a page. The pages that have child pages list them with the ``.. toctree::`` directive. The left navigation that links to each page is built from these lists.

By default the ``.. toctree::`` directive creates both left navigation and in-page navigation links to the child pages. Using ``.. toctree::`` with the ``:hidden:`` option creates left navigation only.

Sphinx requires that the toctree lists include all pages. If a page is not in any toctree list, it is a page with no parent page, or an "orphan" page, and the Sphinx build will fail with an error. If for some reason a page must be in the documentation and must not be in the left navigation, the ``:orphan:`` directive can be added at the top of that page so that Sphinx will build without errors. Please avoid the ``:orphan:`` directive as much as possible.

The optional directive ``.. contents::`` will automatically scan the headers in a page and build an in-page nested table of contents from them. In-page links to the sections of a page make it easier for users to read long pages.

A ``.. contents::`` directive may use the depth option to limit the depth of the nested list. For example, ``:depth: 2`` will build a table of contents that only shows the highest two levels of headers. Use this in pages with many headers to keep the table of contents from being too long and unwieldy.

The :doc:`directory/sphinx` includes more information and examples on ``contents`` and ``toctree``.

Code formatting
===============

Use fixed width or monospace text for inline code. EXAMPLE:

.. code-block:: rst

    Use ``cd tmp`` to change to the ``tmp`` directory.

Use ``cd tmp`` to change to the ``tmp`` directory.

Use the ``.. code-block::`` directive for blocks of code. EXAMPLE:

.. code-block:: rst

    .. code-block:: python

        for i in range(10):
            print(i)

.. code-block:: python

    for i in range(10):
        print(i)

Code blocks can use the types ``python`` ``rst`` ``yaml`` ``bash`` ``none`` and more.

Lists
=====

Use "#" for ordered (numbered) lists and "*" for unordered lists. EXAMPLES:

.. code-block:: rst

    #. First item
    #. Second item

#. First item
#. Second item

.. code-block:: rst

    * Begin your list
    * Split long list items across any
      number of lines
    * Continue your list

      * Use nested lists when appropriate
      * Make sure the spacing is correct

    * Finish your list.

* Begin your list
* Split long list items across any
  number of lines
* Continue your list

  * Use nested lists when appropriate
  * Make sure the spacing is correct

* Finish your list.

Links
=====

reStructuredText supports ordinary links to outside pages. It also has a simpler and more flexible way to link to documents or sections of documents in the current documentation project.

Document links with the ``:doc:`` directive send the reader to the beginning of another page.

Reference links with the ``:ref:`` directive send the reader to another section. The section may be in the current page or another page in the same project. Reference links work like HTML anchor links such as ``file.html#section-one``.

EXAMPLES:

.. code-block:: rst

    Links: http://microsoft.com . `Google <http://google.com>`_. See also :ref:`cheatsheet-alpha` ahead.

    .. _cheatsheet-alpha:

    Section alpha
    -------------

Links: http://microsoft.com . `Google <http://google.com>`_. See also :ref:`cheatsheet-alpha` ahead.

.. _cheatsheet-alpha:

Section alpha
-------------

.. code-block:: rst

    Here is a :ref:`link to another section <cheatsheet-bravo>` up ahead.

    .. _cheatsheet-bravo:

    Section bravo
    -------------

Here is a :ref:`link to another section <cheatsheet-bravo>` up ahead.

.. _cheatsheet-bravo:

Section bravo
-------------

.. code-block:: rst

    For more information refer to :doc:`another document <directory/two>`.

    The link caption defaults to the document title if no other title is given: :doc:`directory/two`

For more information refer to :doc:`another document <directory/two>`.

The link caption defaults to the document title if no other title is given: :doc:`directory/two`

Images
======

Insert images with the ``.. image::`` directive.

To separate the text after an image from the image, insert extra space with a vertical bar character ("|").

EXAMPLE:

.. code-block:: rst

    .. image:: /img/earth.jpg

    |

    Text after the image goes here.

.. image:: /img/earth.jpg

|

Text after the image goes here.

Sphinx can also create tables, embed raw html, and more. For further information please see the :doc:`directory/sphinx`.
