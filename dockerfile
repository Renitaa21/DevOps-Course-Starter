FROM python:3.9.1-slim-buster as base

WORKDIR /todo-app

COPY pyproject.toml poetry.lock ./

#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

#ENV PATH=$PATH:/root/.poetry/bin

#Using curl didnt work so Hugh suggested using pip

RUN pip install poetry && poetry install 

COPY ./todo_app ./todo_app

FROM base as production

CMD ["poetry","run","gunicorn","-b","0.0.0.0:5000","todo_app.app:create_app()"]

EXPOSE 5000

FROM base as development

CMD ["poetry","run","flask","run","--host","0.0.0.0"]

EXPOSE 5000