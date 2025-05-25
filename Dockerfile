FROM python:3.13-slim

WORKDIR /musicbox

COPY . /musicbox

RUN pip install poetry

RUN poetry install --no-root

ENTRYPOINT ["poetry", "run", "python", "manage.py", "runserver"]
