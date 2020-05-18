# STS CLI

A tool for comparing the semantic similarity of two texts from the command line.

## Installation and Usage

The project can be simply be installed via pip. For example in a virtual
environment:
```python
# Create some envrironment to install it to
python3 -m pip install virtualenv
python3 -m venv .venv
source .venv/bin/activate
# Now we can install it
pip install -e .
```

**Attention:**
Make shure you pip version is up to date, since Tensorflow 2 
packages require `pip version > 19.0`, especially if you are using `virtualenv`.
To test out the implementation, it can run on using the CLI:

```shell script
sts "Das ist ein Test" "Das ist ein weiterer Test"
```

## For Windows

This project relies on the python pacakge `tensorflow-text`, which is not available
under windows. To try the project out anyway, a Dockerfile was included, which
lets you run the cli in a Docker Container.

To build the docker container and run it, type
```shell script
cd directory/with/the/Dockerfile
docker build --tag sts-cli .
docker run sts-cli "My first sentence." "My second sentence."
``` 

## Introduction STS and the project

Comparing different text bodies for their semantic similarity is a common, but
in no way trivial task to do. While lexical similarity compares, how similar two
sets of words are on the outside, semantic similarity cares about how similar
both are in meaning. This has even to be the case, if both sentences do not
share many common words.

Semantic Text comparison requires to translate our text into a format, which we
can compare more easily. One such format are for example vectors. By comparing
e.g. the cosinus similarity of two vectors, we can compare how similar their
direction is. With good word embeddings, two texts with very similar meaning
will produce vectors pointing to a very similar direction.

Producing such vectors does not necessarily requires using neural networks.
Bag of Words e.g. can produce such vectors in a statistical way by counting
word occurrences. Machine learning approaches on the other hand proved to be
more accurate.

Options for non statistical embeddings using neural networks:
- For Embedding of individual words: Google's Word2Vec
    - Support for Multiple Languages
    - Models trained in the German language (Wikipedia) already exist

While W2V is good for embedding single words, we need an additional step for
using it with entire sentences (e.g. calculate an average vector from all word
vectors in the sentence).    

- For Embedding of entire Sentences: Google's Universal Sentence Encoder
    - Support for Multiple Languages with multilingual models working with
      16 different languages
    - Can be used at the same time since all of them use the exact same vector
      space
    - Pretrained multilingual models available on TensorflowHub
    - Models can be enhanced, but not trained entirely from scratch (probably we
      would also not have the required amount of annotated data....), see
      [GitHub issue](https://github.com/tensorflow/hub/issues/155)

## Use case specific specialities

Since we are asking for a definition in our use case, a not so small part of the
sentence will always be semantically very similar. A solution for that, which
does not require additional tweeking of the USE model, is to divide the
sentences in relevant and unrelevant parts. For example:

**Question:** What does model XYZ discribe?

**Answer:** Model Xyz discribes that this and that happens to this time.

All given answers will have the part "Model Xyz describes ..." in common, which
improves the similarity score even though we do not care about this particular
part of the sentence. A problem is, that this stripped part can alway look a bit
different in a given answer, so this part can not simply be removed. An easy
solution to get rid of this answer is to alter the question. By providing this
part and asking for a completion, the user will only write the part of the
sentence we are actually interested in.

**Question:** Model Xyz describes ...

**Answer:** ... that this and that happens to this time.

## A less generic approach

It would probably be possible to create a less generic approach by finding a
way to put more stress on parts of the sentence we care about more than others
(e.g. apply some kind of weight-system to individual words). One problem with
such an approach would be, that it would require preparation of all reference
data, which does not seem realistic.

## References and Further Reading

Here I've listed some articles and projects that helped me get into the topic.

- Comparison between different word embeddings and comparison algorithms (
[Repository](https://github.com/adsieg/text_similarity), 
[Medium Article](https://medium.com/@adriensieg/text-similarities-da019229c894)
)
- Introduction into using Word2Vec and Cosinus Similarity (
[Article](https://towardsdatascience.com/a-beginners-guide-to-word-embedding-with-gensim-word2vec-model-5970fa56cc92)) 
- Word2Vec Traning Model using German Wikipedia (
[Documentation](https://devmount.github.io/GermanWordEmbeddings/)
)
- Multilingual Universal Sentence Encoder (
[Medium Article](https://medium.com/@d.salvaggio/multilingual-universal-sentence-encoder-muse-f8c9cd44f171)
[Tensorflow Example Notebook](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/semantic_similarity_with_tf_hub_universal_encoder.ipynb)
[Google AI Blog Article]()
)
