from typing import List
from itertools import combinations_with_replacement
import re

import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text

from .interface import Encoder, SimilarityEvaluator


TF = "https://tfhub.dev/google"
DEFAULT_MODEL_URL = f"{TF}/universal-sentence-encoder-multilingual-large/3"


class MuseEncoder(Encoder):

    def __init__(self,
                 model: str = DEFAULT_MODEL_URL):
        """
        Encoder implementation based on the tensorflow model for the multi-
        lingual universal sentence encoder.
        """
        self._model = hub.load(model)

    def _embed(self, text: str) -> float:
        """Type Check + Embedding model call."""
        if not isinstance(text, str):
            raise TypeError("Only strings are supported for embedding.")
        return self._model(text)

    def extract_features(self, *text: str) -> List[float]:
        """"""
        if len(text) < 2:
            raise ValueError("No text was passed so we have nothing to encode.")
        return [self._embed(t) for t in text]


class CosinusSimilarityEvaluator(SimilarityEvaluator):

    def eval(self, *texts: str) -> np.ndarray:
        results = []
        for t1 in texts:
            results.append([self.eval_pair(t1, t2) for t2 in texts])
        return results

    def eval_pair(self, v1: np.ndarray, v2: np.ndarray) -> float:
        mag1 = np.linalg.norm(v1)
        mag2 = np.linalg.norm(v2)
        if (not mag1) or (not mag2):
            return 0
        return np.dot(np.squeeze(np.asarray(v1)), np.squeeze(np.asarray(v2))) / (mag1 * mag2)