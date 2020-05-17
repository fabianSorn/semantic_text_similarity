curl --location --request GET "https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3?tf-hub-format=compressed" --output model.tar.gz
mkdir model
tar -xzf model.tar.gz -C model
rm model.tar.gz