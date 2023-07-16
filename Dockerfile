# pull base image
FROM python:3.10

# Set Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_USERNAME admin
ENV DJANGO_SUPERUSER_PASSWORD admin
ENV DJANGO_SUPERUSER_EMAIL email@localhost

# Install Dependencies
COPY Pipfile Pipfile.lock /code/
WORKDIR /code
RUN pip install pipenv && pipenv install --system
# copy Project
COPY . /code/

# commands
ENTRYPOINT ["sh", "./entrypoint.sh"]