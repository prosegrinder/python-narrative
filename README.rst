narrative
===========

.. image:: https://img.shields.io/pypi/v/narrative.svg
    :target: https://pypi.python.org/pypi/narrative
    :alt: Latest PyPI version

.. image:: https://github.com/prosegrinder/python-narrative/workflows/Python%20CI/badge.svg?branch=main
    :target: https://github.com/prosegrinder/python-narrative/actions?query=workflow%3A%22Python+CI%22+branch%3Amain
    :alt: GitHub Workflow Status

.. image:: https://api.codacy.com/project/badge/Grade/199d8dcecc4345249c704325bec9cf7c
    :target: https://www.codacy.com/app/ProseGrinder/python-narrative?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=prosegrinder/python-narrative&amp;utm_campaign=Badge_Grade
    :alt: Latest Codacy Coverage Report

A small Python package for splitting text into dialogue and narrative.

Installation
------------

``narrative`` is available on PyPI. Simply install it with ``pip``::

    $ pip install narrative

You can also install it from source::

    $ git clone https://github.com/prosegrinder/python-narrative.git
    Cloning into 'python-narrative'...
    ...

    $ cd python-narrative
    $ python setup.py install
    ...

Usage
-----

``narrative`` splits a piece of prose into narrative and dialogue components. The main function ``split()`` will return a dict containing both ``narrative`` and ``dialogue`` components::

    >>> import narrative
    >>> text = '"Hello," he said. "How are you today?"'
    >>> narrative.split(text)
    {'dialogue': ['"Hello,"', '"How are you today?"'], 'narrative': ['', ' he said. ', '']}

There are two other helper functions as well.

``get_dialogue()`` returns only the dialogue components::

    >>> narrative.get_dialogue(text)
    ['"Hello,"', '"How are you today?"']

``get_narrative()`` returns only the narrative components::

    >>> narrative.get_dialogue(text)
    ['', ' he said. ', '']

Note: The empty strings are a feature of Python's ``split()`` function. See `Why are empty strings returned in split() results?`_ for an explanation.

Authors
-------

``narrative`` was written by `David L. Day <dday376@gmail.com>`_.

.. _`Why are empty strings returned in split() results?`: https://stackoverflow.com/questions/2197451/why-are-empty-strings-returned-in-split-results#2197493
