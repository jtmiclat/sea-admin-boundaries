FROM python:3.9

WORKDIR /app

# install poetry
RUN pip install poetry

# copy poetry files
COPY ./pyproject.toml ./poetry* /app/

# export dependencies to a requirements.txt
RUN poetry export -f requirements.txt --output /requirements.txt  --without-hashes

# run install of python packages
RUN pip install  --no-cache-dir -r /requirements.txt

# copy project files
COPY . /app