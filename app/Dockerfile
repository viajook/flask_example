# pull officail image
FROM python:3.12.1-slim-bullseye
# Expose port 5000
EXPOSE 5000 
#copy the content of the current directory
COPY . /app
# set work directory
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "app.py" ]
