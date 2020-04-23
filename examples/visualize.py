# Source: https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/semantic_similarity_with_tf_hub_universal_encoder.ipynb

import os
import re

import tensorflow as tf
import tensorflow_hub as hub

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

# Source: https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/semantic_similarity_with_tf_hub_universal_encoder.ipynb#scrollTo=BnvjATdy64eR


URL = "https://tfhub.dev/google/universal-sentence-encoder/4"
"""URL to our Tensorflow Module"""


def plot_similarity(labels, features, rotation):
    corr = np.inner(features, features)
    sns.set(font_scale=1.2)
    g = sns.heatmap(
      corr,
      xticklabels=labels,
      yticklabels=labels,
      vmin=0,
      vmax=1,
      cmap="YlOrRd")
    g.set_xticklabels(labels, rotation=rotation)
    g.set_title("Semantic Textual Similarity")
    plt.show()

def run_and_plot(messages_, embed):
    message_embeddings_ = embed(messages_)
    plot_similarity(messages_, message_embeddings_, 90)


if __name__ == "__main__":
    embed = hub.load(URL)
    messages = [
        # Smartphones
        "I like my phone",
        "My phone is not good.",
        "Your cellphone looks great.",
        # Weather
        "Will it snow tomorrow?",
        "Recently a lot of hurricanes have hit the US",
        "Global warming is real",
        # Food and health
        "An apple a day, keeps the doctors away",
        "Eating strawberries is healthy",
        "Is paleo better than keto?",
        # Asking about age
        "How old are you?",
        "what is your age?",
    ]
    run_and_plot(messages, embed)
