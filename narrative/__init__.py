# -*- coding: utf-8 -*-

"""narrative - A small Python package for splitting text into dialogue and narrative."""

import re

import pkg_resources

__version__ = pkg_resources.resource_string(
    'narrative', 'VERSION').decode('utf-8').strip()

# NOTE: Smart quotes are error prone. I recommend converting
# them to regular quotes first.
#
# RegEx developed from following reference
# http://www.rubular.com/r/mP6IRzteSm
# http://pythex.org/
# http://www.metaltoad.com/blog/regex-quoted-string-escapable-quotes
# DIALOGUE_RE = r'[\"“]((?:.(?![\"“]))*.?)[\"”\\n]'
DIALOGUE_RE = re.compile(r'[\"“](?:.(?![\"“]))*.?[\"”\\n]', re.MULTILINE)


def get_dialogue(text, dialogue_regex=DIALOGUE_RE):
    dialogue = dialogue_regex.findall(text)
    return dialogue


def get_narrative(text, dialogue_regex=DIALOGUE_RE):
    narrative = dialogue_regex.split(text)
    return narrative


def split(text, dialogue_regex=DIALOGUE_RE):
    dialogue = get_dialogue(text, dialogue_regex)
    narrative = get_narrative(text, dialogue_regex)
    return {"dialogue": dialogue, "narrative": narrative}
