# narrative

[![Latest PyPI version](https://img.shields.io/pypi/v/narrative.svg)](https://pypi.python.org/pypi/narrative)
[![GitHub Workflow Status](https://github.com/prosegrinder/python-narrative/workflows/Python%20CI/badge.svg?branch=main)](https://github.com/prosegrinder/python-narrative/actions?query=workflow%3A%22Python+CI%22+branch%3Amain)

A small Python package for splitting text into dialogue and narrative.

## Installation

`narrative` is available on PyPI. Simply install it with `pip`:

```bash
pip install narrative
```

You can also install it from source:

```bash
$ git clone https://github.com/prosegrinder/python-narrative.git
Cloning into 'python-narrative'...
...

$ cd python-narrative
$ python setup.py install
...
```

## Usage

`narrative` splits a piece of prose into narrative and dialogue
components. The main function `split()` will return a dict containing
both `narrative` and `dialogue` components:

```python
>>> import narrative
>>> text = '"Hello," he said. "How are you today?"'
>>> narrative.split(text)
{'dialogue': ['"Hello,"', '"How are you today?"'], 'narrative': ['', ' he said. ', '']}
```

There are two other helper functions as well.

`get_dialogue()` returns only the dialogue components:

```python
>>> narrative.get_dialogue(text)
['"Hello,"', '"How are you today?"']
```

`get_narrative()` returns only the narrative components:

```python
>>> narrative.get_dialogue(text)
['', ' he said. ', '']
```

Note: The empty strings are a feature of Python's `split()` function.
See [Why are empty strings returned in split()
results?](https://stackoverflow.com/questions/2197451/why-are-empty-strings-returned-in-split-results#2197493)
for an explanation.
