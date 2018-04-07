# -*- coding: utf-8 -*-

import narrative

EXCERPT = """Some one recklessly lifted the veil. By one breath of an uttered word he destroyed the serene charm, and uncovered the truth in its ugly nakedness. No thought was clearly defined in his mind, when his lips smilingly asked: "Why do you not tell us, Lazarus, what was There?" And all became silent, struck with the question. Only now it seemed to have occurred to them that for three days Lazarus had been dead; and they looked with curiosity, awaiting an answer. But Lazarus remained silent.

"You will not tell us?" wondered the inquirer. "Is it so terrible there?"
"""
# Lazarus by Leonid Andreyev

DIALOGUE = [
    '"Why do you not tell us, Lazarus, what was There?"',
    '"You will not tell us?"',
    '"Is it so terrible there?"'
]

NARRATIVE = [
    "Some one recklessly lifted the veil. By one breath of an uttered word he destroyed the serene charm, and uncovered the truth in its ugly nakedness. No thought was clearly defined in his mind, when his lips smilingly asked: ",
    " And all became silent, struck with the question. Only now it seemed to have occurred to them that for three days Lazarus had been dead; and they looked with curiosity, awaiting an answer. But Lazarus remained silent.\n\n",
    ' wondered the inquirer. ',
    "\n"
]


def test_get_dialogue():
    assert(narrative.get_dialogue(EXCERPT) == DIALOGUE) # nosec


def test_get_narrative():
    assert(narrative.get_narrative(EXCERPT) == NARRATIVE) # nosec


def test_parse():
    assert(narrative.split(EXCERPT) == {"narrative": NARRATIVE, "dialogue": DIALOGUE}) # nosec
