============================
reStructuredText cheat sheet
============================

.. contents::
   :local:

Headings
========

The sections of a page are defined by headings. Typically a page's title is H1, the page's sections are H2 and the subsections are H3.

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

NOTE: Sphinx will actually accept header style it encounters first as H1, the next as H2, and so on, but we prefer to use these styles for consistency.

Tables of contents
==================

We use two types of tables of contents (TOCs):

#. TOCTREE: This organizes the pages and creates a nested list of links to each page in the left navigation.
#. CONTENTS: This creates a nested list of links to sections of the current page as in-page navigation.

Sphinx keeps pages in a `tree data structure <https://en.wikipedia.org/wiki/Tree_(data_structure)>`_ where each node is a page. The pages that have child pages list them with the ``.. toctree::`` directive. The left navigation that links to each page is built from these lists.

By default the ``.. toctree::`` directive creates both left navigation and in-page navigation links to the child pages, and with the ``:hidden:`` option it only creates left navigation.

Sphinx requires that the toctree lists include all pages. If a page is not in any toctree list, it is a page with no parent page, or an "orphan" page, and the Sphinx build will fail with an error. If for some reason a page must be in the documentation and must not be in the left navigation, the ``:orphan:`` directive can be added at the top of that page so that Sphinx will build without errors. Please avoid the ``:orphan:`` directive as much as possible.

The optional directive ``.. contents::`` will automatically scan the headers in a page and build an in-page nested table of contents from them. In-page links to the sections of a page make it easier for users to read long pages.

A ``.. contents::`` directive may use the depth option to limit the depth of the nested list. For example, ``:depth: 2`` will build a table of contents that only shows the highest two levels of headers. Use this in pages with many headers to keep the table of contents from being too long and unwieldy.

The :doc:`Sphinx example file <directory/sphinx>` includes more information on ``contents`` and ``toctree`` and shows examples.

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

    #. Numbered
    #. List

#. Numbered
#. List

.. code-block:: rst

    * Bullet list item one.
    * If bullet list item two is long then it
      can be split across any number of lines.
    * Item three.

      * Nested lists
      * also work.

    * Item four.

* Bullet list item one.
* If bullet list item two is long then it
  can be split across any number of lines.
* Item three.

  * Nested lists
  * also work.

* Item four.

Links
=====

.. code-block:: rst

    Links: http://microsoft.com . `Google <http://google.com>`_. See also :ref:`cheatsheet-alpha` ahead.

Links: http://microsoft.com . `Google <http://google.com>`_. See also :ref:`cheatsheet-alpha` ahead.

.. code-block:: rst

    .. _cheatsheet-alpha:

    Section alpha
    =============

.. _cheatsheet-alpha:

Section alpha
=============

.. code-block:: rst

    Here is a :ref:`link to another section <cheatsheet-bravo>` up ahead.

    .. _cheatsheet-bravo:

    Section bravo
    =============

Here is a :ref:`link to another section <cheatsheet-bravo>` up ahead.

.. _cheatsheet-bravo:

Section bravo
=============

Use the ``:doc:`` directive to link to a document. EXAMPLE:

.. code-block:: rst

    For more information refer to :doc:`another document <directory/two>`.

    The link caption defaults to the document title if no other title is given: :doc:`directory/two`

For more information refer to :doc:`another document <directory/two>`.

The link caption defaults to the document title if no other title is given: :doc:`directory/two`

Reference links are similar to anchor links such as ``file.html#section-one`` and document links are just links to other files.

Images
======

Bars can be used for proper spacing of images in text:

.. image:: img/earth.jpg



Directives
----------

The ref and doc directives for references and documents:

.. code-block:: rst

  This text refers to :ref:`my-reference-label` ahead.

  .. _my-reference-label:

  Section Alpha
  -------------

  This is the text of the section.

  Here is a :ref:`link to another section<label-two>` up ahead.

  .. _label-two:

  Section Bravo
  -------------

  Sphinx supports automatic cross references to :doc:`another document<two>` in the same archive.

  The link caption defaults to the document title if no other title is given: :doc:`two`

  Or with absolute pathname: :doc:`/directory/two`
  
  References are similar to anchor links such as ``file.html#section-one`` and documents 
  are just links to other files.

This text refers to :ref:`my-reference-label` ahead.

.. _my-reference-label:

Section Alpha
-------------

This is the text of the section.

Here is a :ref:`link to another section<label-two>` up ahead.

.. _label-two:

Section Bravo
-------------

Sphinx supports automatic cross references to :doc:`another document<two>` in the same archive.

The link caption defaults to the document title if no other title is given: :doc:`two`

Or with absolute pathname: :doc:`/directory/two`

References are similar to anchor links such as ``file.html#section-one`` and documents 
are just links to other files.

Images
------

This is allowed in rst in general, but produces a 'nonlocal image' warning in sphinx:

.. code-block:: rst

  .. image:: http://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Green_eyes_kitten.jpg/120px-Green_eyes_kitten.jpg

Warnings in a local build will cause Travis CI to fail. So, make sure your images 
are local images. It might also be possible to embed a nonlocal image similarly to 
embedding a YouTube video, as explained below, but embedding nonlocal images is 
probably best avoided anyway. Here's a local image.

To ensure plenty of space between an image and the text after it, you can use a bar.

.. code-block:: rst

  .. image:: Puppy_2.jpg

  |
  
  Text after the image.

.. image:: Puppy_2.jpg

|

Text after the image.
