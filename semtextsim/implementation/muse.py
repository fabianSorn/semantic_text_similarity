import logging
from pathlib import Path
from typing import List

LOGGER = logging.getLogger(__file__)

import numpy as np
# Silence tensorflow with this:
# import os
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf

import tensorflow_text;

do_not_remove = tensorflow_text
"""
Not importing tensorflow_text before loading the universal sentence encoder 
model leads to errors (even if it is not used in this module...)
"""

from semtextsim.interface import Encoder as AbcEncoder


def model_location():
    import semtextsim
    return str(Path(semtextsim.__file__).parent.parent.absolute() / "model" / "muse")


class Encoder(AbcEncoder):

    def __init__(self,
                 model: str = model_location()):
        """
        Encoder implementation based on the tensorflow model for the multi-
        lingual universal sentence encoder.
        """
        try:
            self._model = tf.keras.models.load_model(model)
        except OSError:
            LOGGER.error("The local model could not be loaded. Make sure to run "
                         "'./download_model.sh' to download the model to the "
                         "right place.")
            raise OSError

    def _embed(self, text: str) -> np.ndarray:
        if not isinstance(text, str):
            raise TypeError("Only strings are supported for embedding.")
        return self._model(text)

    def encode(self, *text: str) -> List[np.ndarray]:
        return [self._embed(t) for t in text]
