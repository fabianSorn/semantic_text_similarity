import argparse
import json
import sys
import io
from typing import List, Tuple, Optional
from textwrap import wrap
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from semtextsim.muse_cosinus import MuseEncoder, CosinusSimilarityEvaluator


@dataclass
class Definition:

    question: str
    reference: str
    answers: List[str]
    answer_similarities: Optional[List[float]] = None

    @staticmethod
    def from_json(args: str):
        args = json.loads(args)
        return Definition(args["question"],
                          args["reference"],
                          args["answers"])


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
    parser.add_argument("texts", type=str, nargs='*', default=sys.stdin)
    return parser.parse_args()


def _plot(definition: Definition):
    """Plot the similarity between each of the given sentences. If n sentences
    are passed, a n*n 2D array of similarity scores is expected."""
    sns.set(font_scale=1.2)
    g = sns.heatmap(
        np.array(definition.answer_similarities).reshape(len(definition.answer_similarities), 1),
        vmin=0,
        vmax=1,
        annot=True,
        cmap="YlOrRd")
    g.set_xticklabels(['\n'.join(wrap(l, 40)) for l in [definition.reference]], rotation=0)
    g.set_yticklabels(['\n'.join(wrap(l, 40)) for l in definition.answers], rotation=0)
    g.set_title(definition.question)
    plt.show()


def _read_file(f: str) -> Definition:
    """Read text from the file at the passed location. Sentences can span
    multiple lines and should be separated by a dot."""
    with open(f, "r") as file:
        entire_text = file.read()
        return Definition.from_json(entire_text)


def main():
    args = _args()
    encoder = MuseEncoder()
    evaluator = CosinusSimilarityEvaluator()
    if args.file:
        definition = _read_file(args.file)
    elif isinstance(args.texts, io.TextIOWrapper):
        definition = Definition.from_json(args.texts.read())
    elif len(args.texts) == 1:
        definition = Definition.from_json(args.texts[0])
    else:
        definition = Definition(question="",
                                reference=args.texts.pop(0),
                                answers=args.texts)
    reference_embedding = encoder.extract_features(definition.reference)
    answer_embeddings = encoder.extract_features(*definition.answers)
    similarities = [evaluator.eval_pair(reference_embedding, a) for a in answer_embeddings]
    definition.answer_similarities = similarities
    # print(definition.answer_similarities)
    _plot(definition)


if __name__ == "__main__":
    main()
