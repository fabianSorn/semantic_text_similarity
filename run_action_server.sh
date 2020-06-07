#!/bin/bash
docker run -v $(pwd):/app rasa/rasa:1.10.2-full train