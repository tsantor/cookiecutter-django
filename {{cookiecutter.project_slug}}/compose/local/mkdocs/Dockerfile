FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update -y \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./compose/local/mkdocs/requirements.txt /requirements.txt
RUN pip install -U pip && \
    pip install --no-cache-dir -r /requirements.txt \
    && rm /requirements.txt

COPY ./compose/local/mkdocs/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

WORKDIR /mkdocs

ENTRYPOINT ["/entrypoint"]
