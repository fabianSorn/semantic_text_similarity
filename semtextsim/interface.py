from typing import Any
from abc import ABC, abstractmethod
import numpy as np


class Encoder(ABC):

    def __init__(self):
        """Abstract Base Class defining the interface of a text encoder."""
        pass

    @abstractmethod
    def extract_features(self, text: str) -> Any:
        """
        Extract Features from the given Text. This can be e.g. creating a
        vector representation of them.

        Args:
            text: text, whose features should be extracted.

        Returns:
            Features of the passed text.
        """
        pass


class SimilarityEvaluator:

    def __init__(self):
        """Abstract class defining the interface for comparing the semantics
        of given texts."""
        pass

    @abstractmethod
    def eval_pair(self, text_1: str, text_2: str) -> float:
        """Evaluate the similarity between the two given texts."""
        pass

    @abstractmethod
    def eval(self, *texts: str) -> np.ndarray:
        """Evaluate how semantically similar the given text pieces are."""
        pass

