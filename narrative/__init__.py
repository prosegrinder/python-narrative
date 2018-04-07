# -*- coding: utf-8 -*-

"""narrative - A Python small package for splitting text into dialogue and narrative."""

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
DIALOGUE_RE = r'[\"“]((?:.(?![\"“]))*.?)[\"”\\n]'


def get_dialogue(text, dialogue_regex=DIALOGUE_RE):
    matches = re.finditer(dialogue_regex, text)
    dialogue = [match.group() for matchNum, match in enumerate(matches)]
    return dialogue


def get_narrative(text, dialogue_regex=DIALOGUE_RE):
    narrative = dialogue_regex.split(text)
    return narrative


def parse(text, dialogue_regex=DIALOGUE_RE):
    dialogue = get_dialogue(text, dialogue_regex)
    narrative = get_narrative(text, dialogue_regex)
    return {"dialogue": dialogue, "narrative": narrative}
