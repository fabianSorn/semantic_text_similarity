#!/bin/sh

folder="model"
archive="${folder}.tar.gz"

# Remove any old models
rm -rf $folder 2> /dev/null
rm $archive 2> /dev/null

# Download model archive from tensorflow hub
curl --location --request GET "https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3?tf-hub-format=compressed" --output $archive

# Unpack downloaded model into folder
mkdir $folder
tar -xzf $archive -C $folder
rm $archive