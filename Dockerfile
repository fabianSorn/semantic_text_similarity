FROM tensorflow/tensorflow
ARG MODEL_URL="https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3?tf-hub-format=compressed"
RUN mkdir home/application
WORKDIR home/application

# Copy only the neccessary files
ADD semtextsim ./semtextsim
ADD setup.cfg .
ADD setup.py .

# ADD does not seem to work properly for tensorflow models, so we do it by hand
RUN curl --location --request GET $MODEL_URL --output model.tar.gz
RUN mkdir model
RUN tar -xzf model.tar.gz -C model
RUN rm model.tar.gz

# Now install the project and define it as the entry point
RUN pip install -e .
ENTRYPOINT ["sts"]