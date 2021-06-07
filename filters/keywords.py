import spacy

from interfaces.SentenceOperation import SentenceOperation
from tasks.TaskTypes import TaskType
from typing import List

class TextContainsKeywordsFilter(SentenceOperation):
    tasks = [TaskType.TEXT_CLASSIFICATION, TaskType.TEXT_TO_TEXT_GENERATION]
    locales = ["en"]

    def __init__(self, keywords: List[str]):
        super().__init__()
        self.keywords = keywords
        self.nlp = spacy.load('en_core_web_sm')

    def apply(self, sentence: str) -> bool:
        tokenized = self.nlp(sentence, disable=['parser', 'tagger', 'ner'])
        contained_keywords = set(tokenized).intersection(set(self.keywords))
        return bool(contained_keywords)