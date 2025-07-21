# -*- coding: utf-8 -*-

"""narrative

A small Python package for splitting text into dialogue and narrative.
"""

import re

from importlib import metadata
from typing import Final

__version__ = metadata.version(__name__)

# NOTE: Smart quotes are error prone. I recommend converting
# them to regular quotes first.
#
# RegEx developed from following reference
# http://www.rubular.com/r/mP6IRzteSm
# http://pythex.org/
# http://www.metaltoad.com/blog/regex-quoted-string-escapable-quotes
# DIALOGUE_RE = r'[\"“]((?:.(?![\"“]))*.?)[\"”\\n]'
DIALOGUE_RE: Final[re.Pattern] = re.compile(
    r"[\"“](?:.(?![\"“]))*.?[\"”\\n]", re.MULTILINE
)

BRITISH_DIALOGUE_RE: Final[re.Pattern] = re.compile(
    r"['‘](?:.(?!['‘]))*.?['’\n]", re.MULTILINE
)


def get_dialogue(text: str, dialogue_regex: re.Pattern = DIALOGUE_RE) -> list[str]:
    """Get the dialogue fragments from a piece of text

    Parameters:
    ----------
    text : str
        a block of english language text
    dialogue_regex : re.Pattern, optional
        a regular expression to match dialogue fragments,
        by default DIALOGUE_RE

    Returns:
    -------
    list[str]
        a list of dialogue fragments found in the text
    """
    dialogue = dialogue_regex.findall(text)
    return dialogue


def get_narrative(text: str, dialogue_regex: re.Pattern = DIALOGUE_RE) -> list[str]:
    """Get the narrative fragments from a piece of text

    Parameters:
    ----------
    text : str
        a block of english language text
    dialogue_regex : re.Pattern, optional
        a regular expression to match dialogue fragments,
        by default DIALOGUE_RE

    Returns:
    -------
    list[str]
        a list of narrative fragments found in the text
    """
    narrative = dialogue_regex.split(text)
    return narrative


def split(text: str, dialogue_regex: re.Pattern = DIALOGUE_RE) -> dict[str, list[str]]:
    """Split a piece of text into dialogue and narrative

    Parameters:
    ----------
    text : str
        a block of english language text
    dialogue_regex : re.Pattern, optional
        a regular expression to match dialogue fragments,
        by default DIALOGUE_RE

    Returns:
    -------
    dict
        a dict with a list of dialogue and and a list of
        narrative found in the text

            {
                "dialogue": list[str],
                "narrative": list[str],
            }
    """
    dialogue = get_dialogue(text, dialogue_regex)
    narrative = get_narrative(text, dialogue_regex)
    return {"dialogue": dialogue, "narrative": narrative}
