FROM tensorflow/tensorflow
RUN mkdir home/application
WORKDIR home/application

# Copy only the neccessary files
ADD semtextsim ./semtextsim
ADD setup.cfg .
ADD setup.py .

# Download model so we do not have to rely on tensorflow_hub package
ADD download_model.sh .
RUN chmod a+x download_model.sh && ./download_model.sh && rm download_model.sh

# Now install the project and define it as the entry point
RUN pip install -e .[server]
EXPOSE 8000

# --host 0.0.0.0 -> listen on all network interfaces of the docker container
CMD ["uvicorn", "semtextsim.user_interfaces.rest:app", "--host", "0.0.0.0", "--port", "8000"]