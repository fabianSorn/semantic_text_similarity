from typing import List, Tuple
import random


class DefintionTester:

    terms: List[Tuple[str, str]] = [
        ("Präattentive Wahrnehmung", "Die Präattentive Wahrnehmung ist eine " \
                                     "vorbewusste, unterschwellige " \
                                     "Wahrnehmung von Sinnesreizen")
    ]

    def __init__(self):
        """Class which asks for the definition of a term and allows compare a
        self written string answer to it."""
        self._comparer = Comparer()
        self._current_term = None
        self._update_term()

    @property
    def current_term(self):
        """The current term."""
        return self._current_term[0]

    @property
    def current_definition(self):
        """Definition of the current term."""
        return self._current_term[1]

    def definition_question(self) -> str:
        """Get a question asking for the definition of a term. Each call you
        will get a question asking for a new term."""
        self._update_term()
        return f"Please explain {self._current_term[0]}."

    def compare_answer(self, answer: str) -> float:
        """Return a percentage (0.0 -> 1.0) how well the given answer matches
        the known definition of the term."""
        return 0.0

    def _update_term(self) -> None:
        """Choose a new term with its defintion"""
        index = random.uniform(0, len(MockChatbot.terms) - 1)
        self._current_term = MockChatbot.terms[index]

