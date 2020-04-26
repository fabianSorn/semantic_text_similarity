import argparse
from typing import List
from textwrap import wrap
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from .muse_cosinus import MuseEncoder, CosinusSimilarityEvaluator


def _args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",
                        "--file",
                        help="File-Path containing sentences to compare.")
    parser.add_argument("-i",
                        "--implementation",
                        choices=["MuseCos"],
                        help="Choose the implementation to use")
    parser.add_argument("-p",
                        "--plot",
                        action="store_true",
                        help="Plots the similarities of the given sentences.")
    parser.add_argument("texts", type=str, nargs='*')
    return parser.parse_args()


def _plot(sentences: List[str], similarity: np.ndarray):
    sns.set(font_scale=1.2)
    g = sns.heatmap(
      similarity,
      xticklabels=[ '\n'.join(wrap(l, 30)) for l in sentences ],
      yticklabels=[ '\n'.join(wrap(l, 30)) for l in sentences ],
      vmin=0,
      vmax=1,
      cmap="YlOrRd")
    g.set_xticklabels([ '\n'.join(wrap(l, 20)) for l in sentences ], rotation=90)
    g.set_title("Semantic Textual Similarity")
    plt.show()


def main():
    args = _args()
    encoder = MuseEncoder()
    evaluator = CosinusSimilarityEvaluator()
    results = None
    sentences = None
    if args.file is not None:
        with open(args.file, "r") as file:
            sentences = [f.replace("\n", "") for f in file.readlines()]
    elif len(args.texts) >= 2:
        sentences = args.texts
    else:
        raise ValueError("Can't compare. Either pass two strings or a file.")
    results = evaluator.eval(*encoder.extract_features(*sentences))
    if args.plot:
        _plot(sentences, results)
    else:
        for i, s1 in enumerate(sentences):
            for j, s2 in enumerate(sentences):
                print(f'"{s1}" <-> "{s2}" match by {int(100 * results[i][j])}%.')
