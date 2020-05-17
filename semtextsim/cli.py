import argparse
from typing import List
from textwrap import wrap
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from .muse_cosinus import MuseEncoder, CosinusSimilarityEvaluator


def _args() -> argparse.Namespace:
    """Set up arguments for the argument parser and return namespace with
    values for these arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",
                        "--file",
                        help="File-Path containing sentences to compare.")
    parser.add_argument("-i",
                        "--implementation",
                        choices=["MuseCos"],
                        help="Choose the implementation to use")
    parser.add_argument("texts", type=str, nargs='*')
    return parser.parse_args()


def _plot(sentences: List[str], similarity: np.ndarray):
    """Plot the similarity between each of the given sentences. If n sentences
    are passed, a n*n 2D array of similarity scores is expected."""
    sns.set(font_scale=1.2)
    g = sns.heatmap(
        similarity,
        xticklabels=['\n'.join(wrap(l, 30)) for l in sentences],
        yticklabels=['\n'.join(wrap(l, 30)) for l in sentences],
        vmin=0,
        vmax=1,
        annot=True,
        cmap="YlOrRd")
    g.set_xticklabels([ '\n'.join(wrap(l, 20)) for l in sentences ], rotation=90)
    g.set_title("Semantic Textual Similarity")
    plt.show()


def _read_file(f: str) -> List[str]:
    """Read text from the file at the passed location. Sentences can span
    multiple lines and should be seperated by a dot."""
    with open(f, "r") as file:
        entire_text = file.read()
        clean = lambda s: s.replace("\n", " ").replace("  ", " ").strip()
        sentences = [clean(f) for f in entire_text.split(".")]
        sentences = [f for f in sentences if len(f.strip()) > 0]
        return sentences


def main():
    args = _args()
    encoder = MuseEncoder()
    evaluator = CosinusSimilarityEvaluator()
    results = None
    sentences = _read_file(args.file) if args.file else args.texts
    if len(sentences) < 2:
        raise ValueError("We need at least two texts to compare.")
    results = evaluator.eval(*encoder.extract_features(*sentences))
    _plot(sentences, results)
