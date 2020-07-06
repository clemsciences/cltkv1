"""Code for sentences tokenization: Old Norse.

Sentence tokenization for Old Norse is available using a regular-expression based tokenizer.

>>> from cltk.sentence.non import OldNorseRegexSentenceTokenizer
>>> from cltk.languages.example_texts import get_example_text
>>> splitter = OldNorseRegexSentenceTokenizer()
>>> sentences = splitter.tokenize(get_example_text("non"))
>>> sentences[:2]

>>> len(sentences)

"""

__author__ = ["Patrick J. Burns <patrick@diyclassics.org>"]


from cltk.sentence.sentence import BaseRegexSentenceTokenizer
from cltk.tokenizers.non import OldNorseLanguageVars


class OldNorseRegexSentenceTokenizer(BaseRegexSentenceTokenizer):
    """``RegexSentenceTokenizer`` for Old Norse."""

    def __init__(self: object):
        super().__init__(
            language="old-norse", sent_end_chars=OldNorseLanguageVars.sent_end_chars
        )
