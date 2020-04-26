"""Top-level package for SemTextSim."""

__author__ = """Fabian Sorn"""
__email__ = 'fabian.sorn@icloud.com'
__version__ = '0.1.0'

from .muse_cosinus import (MuseEncoder,
                           CosinusSimilarityEvaluator)
from .cli import main
