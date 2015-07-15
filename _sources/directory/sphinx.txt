Main Sphinx Example File
========================

.. contents::


Welcome! This Sphinx reference file shows ReStructured Text (rst) code followed
by its html output.

Basic formatting
----------------

.. code-block:: rst

  Paragraphs that spread across
  multiple lines in the source file
  will display on one line in the
  built html file.
  
  The source file uses two line breaks
  to indicate a paragraph break.

Paragraphs that spread across
multiple lines in the source file
will display on one line in the
built html file.

The source file uses two line breaks
to indicate a paragraph break.

.. code-block:: rst

  a *italic* b **bold** c ``literal`` d

a *italic* b **bold** c ``literal`` d


.. code-block:: rst

  a :emphasis:`emphasis` b :strong:`strong` c :literal:`literal`
  d :subscript:`subscript` e :superscript:`superscript` f 
  :title-reference:`title-reference` g

a :emphasis:`emphasis` b :strong:`strong` c :literal:`literal`
d :subscript:`subscript` e :superscript:`superscript` f 
:title-reference:`title-reference` g


character escaping with backslashes: ``thisis\ *one*\ word`` displays as thisis\ *one*\ word

escaping backslashes: ``o\\o/o`` displays as o\\o/o

.. code-block:: rst

  * bullet list
  * with a very long second item 
    on two lines.

* bullet list
* with a very long second item 
  on two lines.


.. code-block:: rst

  1. numbered
  2. list

1. numbered
2. list


.. code-block:: rst

  #. another numbered
  #. list

#. another numbered
#. list


.. code-block:: rst

  * bullet
  * list

    * with
    * nesting

  * which then continues


* bullet
* list

  * with
  * nesting

* which then continues


.. code-block:: rst

  This is a paragraph split across
  two lines.

    This is an indented paragraph
    below it.

  Here is another left justified paragraph.

  | This paragraph with line blocks
  | has line breaks in the html output
  | just as it does in the rst input.

  .. This is a comment.

  ..
     This whole indented block
     is a comment.

     Still in the comment.

  Now out of the comment.




This is a paragraph split across
two lines.

  This is an indented paragraph
  below it.

Here is another left justified paragraph.

| This paragraph with line blocks
| has line breaks in the html output
| just as it does in the rst input.

.. This is a comment.

..
   This whole indented block
   is a comment.

   Still in the comment.

Now out of the comment.

Code blocks
-----------

rst
^^^

Next we'll show how we're displaying these blocks of rst code:

.. code-block:: rst

  .. code-block:: rst

    This is a paragraph split across
    two lines.


.. code-block:: rst

  This is a paragraph split across
  two lines.

HTML
^^^^

.. code-block:: rst

  .. code-block:: html

    <html>
      <head>Hello!</head>
      <body>Hello, world!</body>
    </html>


.. code-block:: html

  <html>
    <head>Hello!</head>
    <body>Hello, world!</body>
  </html>


YAML
^^^^

.. code-block:: rst

  .. code-block:: yaml

    envs_dirs:
      - ~/my-envs
      - /opt/anaconda/envs


.. code-block:: yaml

  envs_dirs:
    - ~/my-envs
    - /opt/anaconda/envs


bash
^^^^

.. code-block:: rst

  .. code-block:: bash

    ls
    pwd
    touch a.txt

.. code-block:: bash

  ls
  pwd
  touch a.txt


python
^^^^^^

.. code-block:: rst

  .. code-block:: python

    for i in range(10):
      print(i)

.. code-block:: python

  for i in range(10):
    print(i)


none
^^^^

If no other type applies, use "none". It can be useful for 
obscure languages or mixtures of languages like this mix of
bash and python.

.. code-block:: rst

  .. code-block:: none

    cat program.py

    for i in range(10):
        print(i)

.. code-block:: none

  cat program.py

  for i in range(10):
      print(i)


Tables
------

Grid table with header:

.. code-block:: rst

  +----------+-----------+-------+
  | a        | b         | c     |
  +==========+===========+=======+
  | north    | north     | north |
  | west     |           | east  |
  +----------+-----------+-------+
  | west     | center    | east  |
  +----------+-----------+-------+
  | south    | south     | south |
  | west     |           | east  |
  +----------+-----------+-------+

+----------+-----------+-------+
| a        | b         | c     |
+==========+===========+=======+
| north    | north     | north |
| west     |           | east  |
+----------+-----------+-------+
| west     | center    | east  |
+----------+-----------+-------+
| south    | south     | south |
| west     |           | east  |
+----------+-----------+-------+


Grid table without:

.. code-block:: rst

  +----------+-----------+-------+
  | north    | north     | north |
  | west     |           | east  |
  +----------+-----------+-------+
  | west     | center    | east  |
  +----------+-----------+-------+
  | south    | south     | south |
  | west     |           | east  |
  +----------+-----------+-------+

+----------+-----------+-------+
| north    | north     | north |
| west     |           | east  |
+----------+-----------+-------+
| west     | center    | east  |
+----------+-----------+-------+
| south    | south     | south |
| west     |           | east  |
+----------+-----------+-------+

"Simple tables" are easier to write, but must have 
more than one row, and the first column cannot contain multiple lines:

.. code-block:: rst

  =====  =====  =======
  A      B      A and B
  =====  =====  =======
  False  False  False
  True   False  False
  False  True   False
  True   True   True
  =====  =====  =======

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

Links
-----

.. code-block:: rst

  http://microsoft.com

  `Google <http://google.com>`_

  This paragraph links to `the yahoo site`_.

  .. _the yahoo site: http://yahoo.com/

http://microsoft.com

`Google <http://google.com>`_

This paragraph links to `the yahoo site`_.

.. _the yahoo site: http://yahoo.com/


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

  Sphinx supports automatic cross references to :doc:`a document called two<two>` in the same archive.

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

Path names
----------

A document at the path ``/sketches/index`` could refer to the document ``/people`` by 
absolute name as ``:doc:`/people``` or by relative name as ``:doc:`../people``` and 
could refer to ``/sketches/parrot`` by absolute name as ``:doc:`/sketches/parrot``` or 
by relative name as ``:doc:`parrot```.

Headers
-------

Usually # signs over and under a title are only ever used to indicate Part One, 
Part Two, and so on in a book, and * signs over and under a title only for chapters 
in a book. This is the complete code of :doc:`two`, which shows those, and typical 
headers from one to five, although it's rare to use more than the third header size.

.. code-block:: rst

  ############
  Document Two
  ############

  .. contents:: Table of Contents
     :depth: 2

  ***********
  Chapter One
  ***********

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

  Text.

Much more typical in our documentation are the headers in this file. Here are its 
first few lines:

.. code-block:: rst

  Main Sphinx Example File
  ========================

  .. contents::


  Welcome! This Sphinx reference file shows ReStructured Text (rst) code followed
  by its html output.

  Basic formatting
  ----------------

  .. code-block:: rst

    Paragraphs that spread across
    multiple lines in the source file
    will display on one line in the
    built html file.
    
    The source file uses two line breaks
    to indicate a paragraph break.

  Paragraphs that spread across
  multiple lines in the source file
  will display on one line in the
  built html file.

  The source file uses two line breaks
  to indicate a paragraph break.

Table of contents
-----------------

As you can see above, this file uses simply ``.. contents::`` for its table of contents. 
Please go look at the table of contents at the top of the file to see how that displays, 
then return here.

:doc:`two` uses this table of contents:

.. code-block:: rst

  .. contents:: Table of Contents
     :depth: 2

The title "Table of Contents" overrides the default title "Contents". The depth 
option specifies that only the two top levels of headers should be displayed
in the table of contents. Please look at :doc:`two` to see how that displays, 
then return here.

Index files
-----------

Instead of using the ``contents`` directive to show a table of its own contents, 
the index file uses the ``toctree`` directive to show a table of other files. 
All files in the archive should be reachable from the toctrees in the index. Files 
can also contain toctrees of their own, which can lead to other files not referenced 
directly by the index. Toctrees may be hidden, and one of the three toctrees in the 
index of this repository is hidden. Please read this code block showing the entire rst 
source code for the index file, then go look at the :doc:`index page<../index>`, then 
return here.

.. code-block:: rst

  .. sphinx documentation master file, created by
     sphinx-quickstart on Mon Jun  1 16:59:11 2015.
     You can adapt this file completely to your liking, but it should at least
     contain the root `toctree` directive.

  Sphinx repository
  =================

  Welcome to the Continuum Analytics notes and examples for Sphinx, TravisCI, GitHub, and our documentation system!

  Instead of using the table of contents below, please start by going directly to the :doc:`directory/sphinx`.


  First Section
  -------------

  First text.


  Second Section
  --------------

  Second text.


  First Set of Documents
  ----------------------

  .. toctree::
     :maxdepth: 2

     dummya
     dummyb


  Second Set
  ----------

  .. toctree::
     :maxdepth: 2

     directory/sphinx
     directory/two


  .. toctree::
     :hidden:
     
     dummyc
     dummyd


  Indices and tables
  ==================

  * :ref:`genindex`
  * :ref:`search`


Images
------

This is allowed in rst in general, but produces a 'nonlocal image' warning in sphinx:

.. code-block:: rst

  .. image:: http://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Green_eyes_kitten.jpg/120px-Green_eyes_kitten.jpg

Warnings in a local build will cause Travis CI to fail. So, make sure your images 
are local images. It might also be possible to embed a nonlocal image similarly to 
embedding a YouTube video, as explained below, but embedding nonlocal images is 
probably best avoided anyway. Here's a local image.

.. code-block:: rst

  .. image:: Puppy_2.jpg

.. image:: Puppy_2.jpg


Downloadable files
------------------

Files marked for download will be copied from their place in the source directory 
to build/html/_downloads , and duplicate filenames are handled.

.. code-block:: rst

   See :download:`this example script <../example.py>`.

See :download:`this example script <../example.py>`.

Notes
-----

.. code-block:: rst

  .. note:: This is a note admonition.
     This is the second line of the first paragraph.

     - The note contains all indented body elements
       following.
     - It includes this bullet list.

.. note:: This is a note admonition.
   This is the second line of the first paragraph.

   - The note contains all indented body elements
     following.
   - It includes this bullet list.

YouTube videos (and other raw html in rst files)
------------------------------------------------

On YouTube you can click "share" and then "embed", and it will show iframe code like this.

.. code-block:: rst

  .. raw:: html

          <iframe width="560" height="315" src="https://www.youtube.com/embed/UaIvrDWrIWM" frameborder="0" allowfullscreen></iframe>

.. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/UaIvrDWrIWM" frameborder="0" allowfullscreen></iframe>


References
----------

intro to sphinx http://docs.writethedocs.org/tools/sphinx/

rst primer http://sphinx-doc.org/rest.html

first steps w sphinx http://sphinx-doc.org/tutorial.html

links http://sphinx-doc.org/markup/inline.html#ref-role

downloads http://sphinx-doc.org/markup/inline.html#referencing-downloadable-files

http://reinout.vanrees.org/weblog/2009/10/30/restructured-text-cheat-sheet.html

RST cheat sheet http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html
