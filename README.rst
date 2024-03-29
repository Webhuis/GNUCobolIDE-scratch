GNUCobolIDE
------------

**GNUCobolIDE is no longer maintained**, see https://github.com/GNUCobolIDE/GNUCobolIDE/issues/439

Features:
---------

- COBOL syntax highlighter
- COBOL code completion
- COBOL code folding
- configurable margins
- navigable tree view of division, sections, paragraphs etc (fully synchronised
  with the code folding panel)
- auto-indentation
- tool for computing PIC fields offsets
- compile as a program (.exe) or as a subprogram (.so/.dll)
- run the program from the editor or from a configurable external terminal (
  necessary if you are using the SCREEN section).
- dark color schemes and theme
- cross platform: works on **GNU/Linux**, **Windows** and **Mac OSX**
- dbpre integration on Linux, esqlOC on Windows


License
-------

GNUCobolIDE is released under the **GPL** version 3


Dependencies
------------

- `GnuCOBOL`_
- `Python3`_ >= 3.3
- `PyQt5`_ (preferred) or `PyQt4`_
- `setuptools`_

*Starting from v4.7, the following pure python dependencies are bundled with OCIDE (this makes packaging easier):*

- `pyqode.qt`_
- `pyqode.core`_
- `pyqode.cobol`_
- `Pygments`_
- `qdarkstyle`_
- `keyring`_
- `githubpy`_


Installation
------------

GNU/Linux
#########

*Note: starting from v4.6.2, the installed executable name is lowercase: gnucobolide*

Ubuntu
++++++

A debian package is available here: https://launchpad.net/cobcide/+download

This package should work on any Ubuntu version >= 14.04 and on any version
derived from Ubuntu.

Fedora
++++++

A RPM package for Fedora 23 is available here: https://launchpad.net/cobcide/+download


ArchLinux
+++++++++

GNUCobolIDE is available from the `AUR`_.

You can install using one of the many available AUR helper; e.g. using yaourt::

    yaourt -S gnucobolide

KaOS
++++

GNUCobolIDE is up in the KaOs Community Packages (KCP)::

    kcp -i gnu-cobol
    kcp -i gnucobolide


Other distributions
+++++++++++++++++++

Install Python3, PyQt5, GnuCOBOL and pip for Python3 using your package manager, then run the following commands::

    sudo pip3 install GNUCobolIDE --upgrade


Note that if you have both PyQt5 and PyQt4 on your system, the IDE will use
PyQt5 by default. To force the use of PyQt4, you should set the
``QT_API`` environment variable to ``pyqt4``.


Windows
#######

There is a windows installer available here: https://launchpad.net/cobcide/+download

Mac OSX
#######

There is a dmg image available here: https://launchpad.net/cobcide/+download

Before running the app, you first have to install the GnuCOBOL compiler, e.g.
using homebrew::

    brew install gnu-cobol


If you installed the compiler in a non-standard path and it is not recognized
by the IDE, you can specify the path to the compiler in the preferences
dialog (``Compiler`` tab)


Resources
---------

-  `Downloads`_
-  `Source repository`_
-  `Issue tracker`_
-  `Documentation`_


Screenshots
-----------

* Home page:

.. image:: https://raw.githubusercontent.com/GNUCobolIDE/GNUCobolIDE/master/doc/source/_static/Home.png
    :align: center

* Editor:

.. image:: https://raw.githubusercontent.com/GNUCobolIDE/GNUCobolIDE/master/doc/source/_static/MainWindow.png
    :align: center

* Code folding:

.. image:: https://raw.githubusercontent.com/GNUCobolIDE/GNUCobolIDE/master/doc/source/_static/Folding.png
    :align: center

* Offset calculator

.. image:: https://raw.githubusercontent.com/GNUCobolIDE/GNUCobolIDE/master/doc/source/_static/PicOffsets.png
    :align: center


* Dark style support

.. image:: https://raw.githubusercontent.com/GNUCobolIDE/GNUCobolIDE/master/doc/source/_static/Dark.png
    :align: center


.. _PyQt4: http://www.riverbankcomputing.co.uk/software/pyqt/download
.. _Downloads: https://launchpad.net/cobcide/+download
.. _Source repository: https://github.com/GNUCobolIDE/GNUCobolIDE/
.. _Issue tracker: https://github.com/GNUCobolIDE/GNUCobolIDE/issues?state=open
.. _Documentation: http://gnucobolide.readthedocs.org/en/latest/
.. _Pygments: http://pygments.org/
.. _pyqode.core: https://github.com/pyQode/pyqode.core/
.. _pyqode.cobol: https://github.com/pyQode/pyqode.cobol/
.. _pyqode.qt: https://github.com/pyQode/pyqode.qt/
.. _GnuCOBOL: http://sourceforge.net/projects/open-cobol/
.. _setuptools: https://pypi.python.org/pypi/setuptools
.. _Python3: http://python.org/
.. _PyQt5: http://www.riverbankcomputing.co.uk/software/pyqt/download
.. _qdarkstyle: https://github.com/ColinDuquesnoy/QDarkStyleSheet
.. _pyQode: https://github.com/pyQode/
.. _githubpy: https://pypi.python.org/pypi/githubpy
.. _keyring: https://pypi.python.org/pypi/keyring
.. _HackEdit: https://github.com/HackEdit/hackedit
.. _AUR: https://aur.archlinux.org/packages/gnucobolide/
