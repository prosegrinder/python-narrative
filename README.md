# narrative

[![Latest PyPI version](https://img.shields.io/pypi/v/narrative.svg)](https://pypi.python.org/pypi/narrative)
[![Python Poetry CI](https://github.com/prosegrinder/python-narrative/actions/workflows/python-ci.yml/badge.svg)](https://github.com/prosegrinder/python-narrative/actions/workflows/python-ci.yml)

A small Python package for splitting text into dialogue and narrative.

## Installation

`narrative` is available on PyPI. Simply install it with `pip`:

```bash
pip install narrative
```

## Usage

`narrative` splits a piece of prose into narrative and dialogue components. The
main function `split()` will return a dict containing both `narrative` and
`dialogue` components:

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
>>> narrative.get_narrative(text)
['', ' he said. ', '']
```

Note: The empty strings are a feature of Python's `split()` function. See
[Why are empty strings returned in split() results?](https://stackoverflow.com/questions/2197451/why-are-empty-strings-returned-in-split-results#2197493)
for an explanation.

### British Style

Each function accepts a second parameter of a regular expression used to parse
out the dialogue. This defaults to `narrative.DIALOGUE_RE`, which follows the
American standard of using double quotes for initial quotes. `narrative` now
includes a second regular expression, `narrative.BRITISH_DIALOGUE_RE`, which
follows the British style of using single quotes for initial quotes. Simply use
it as the second parameter for any function:

```python
>>> import narrative
>>> narrative.split(text, narrative.BRITISH_DIALOGUE_RE)
>>> …
>>> narrative.get_dialogue(text, narrative.BRITISH_DIALOGUE_RE)
>>> …
>>> narrative.get_narrative(text, narrative.BRITISH_DIALOGUE_RE)
>>> …
```
