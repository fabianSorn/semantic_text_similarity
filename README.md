# Semantic Text Similarity Server + CLI

A tool for comparing the semantic similarity of two texts which can be accessed
from the command line or as a webservice.

## Installation and Usage without Docker

To install the project via pip in your environment, run the following commands
in your terminal.

### Preparations (if you are not using docker)

These preparations are mainly necessary for running the project without using
docker.

Optional: Create a local development environment.
```shell script
python -m pip install virtualenv
python -m venv .venv
source .venv/bin/activate
```
`tensorflow >= 2.0` requires `pip >= 19.0`. To make sure your package manager
is up to date, run the following command.
```shell script
pip install --upgrade pip
```

*** The project requires the package
[tensorflow-text](https://pypi.org/project/tensorflow-text/), which is not
available for windows yet. To run the sproject, use the provided docker image. ***

### Installation using pip

```shell script
pip install -e .[cli]
```
```shell script
pip install -e .[server]
```
```shell script
pip install -e .[all]
```

### Usage

When installed correctly, the project can be accessed directly from the command
line. As an example, run the following commands in your terminal.
```shell script
sts "This parrot is no more." "A tiger ... in Africa?"
sts -f examples/absolute_eingabe.json
```

## Web Service

The project can be used as a REST webservice based on
[fastapi](https://fastapi.tiangolo.com) which is served on the ASGI server 
[uvicorn](http://www.uvicorn.org).

To install the requirements and run the server, run the following commands in
your terminal.

```shell script
pip install -e .[server]
sts-server
```

The server offers a single endpoint `/compare`, which handles POST requests
containing two sentences in the body. For learning more about the usage, run
sthe `sts-server` and open 
[http://localhost:8000/redocs](http://localhost:8000/redocs) in your browser.
When called correctly, it will return the similarity percentage as a response.

### Installation and Usage using Docker

A Docker image is provided for running the server.
To build the image, run the following commands in your terminal:

```shell script
docker build -t sts-server .
```

The built container can be started running the following commands in your
terminal:

```shell script
docker run -p 8000:8000 sts-server
```

Then the webservice can be accessed at
[http://localhost:8000](http://localhost:8000)

# Further, more general reading

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
