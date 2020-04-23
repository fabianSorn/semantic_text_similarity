from typing import List
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
import re
from .comparer_interface import Encoder, SimilarityEvaluator


TF = "https://tfhub.dev/google"
DEFAULT_MODEL_URL = f"{TF}/universal-sentence-encoder-multilingual-large/3"


class MultilingualUniversalSentenceEncoder(Encoder):

    def __init__(self,
                 model: str = DEFAULT_MODEL_URL)
        """
        Encoder implementation based on the tensorflow model for the multi-
        lingual sentence encoder.
        """
        self._embed = hub.load(model)

    def extract_features(self, text: str) -> Any:
        self._embed(text)


class CosinusSimilarityEvaluator(SimilarityEvaluator):

    def eval(self, *texts):
        mag1 = np.linalg.norm(v1)
        mag2 = np.linalg.norm(v2)
        if (not mag1) or (not mag2):
            return 0
        return np.dot(v1, v2) / (mag1 * mag2)
