FROM python:3.9-alpine

WORKDIR /app

COPY pyproject.toml poetry.lock README.md /app/
COPY ./migra /app/migra
COPY ./schemainspect /app/schemainspect
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN apk add --update --no-cache --upgrade postgresql-libs
RUN apk add --no-cache --virtual=build-dependencies build-base postgresql-dev
RUN pip install --no-cache-dir packaging psycopg2-binary
RUN pip install .
RUN apk del build-dependencies
RUN rm -rf /app /tmp/* /var/tmp/* /var/cache/apk/*

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["migra", "--help"]