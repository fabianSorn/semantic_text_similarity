from typing import Sequence
from abc import ABC, abstractmethod


class Encoder(ABC):

    """Abstract Base Class defining the interface of a text encoder."""

    @abstractmethod
    def encode(self, *texts: str) -> Sequence[Sequence[float]]:
        """
        Encode the given texts.

        Returns:
            Vector representation of the given texts.
        """
        pass


class Comparer(ABC):

    """
    Abstract class defining the interface for comparing the semantics
    of given texts.
    """

    @abstractmethod
    def compare(self, t1: Sequence[float], t2: Sequence[float]) -> float:
        """Evaluate the similarity between the two given texts."""
        pass

    @abstractmethod
    def compare_all(self, *texts: Sequence[float]) -> Sequence[Sequence[float]]:
        """
        Evaluate the similarity for each of the given texts with each other
        and return their similarity scores in a 2D array.
        """
        pass

