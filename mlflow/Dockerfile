FROM continuumio/miniconda:4.5.4

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN echo "export LC_ALL=$LC_ALL" >> /etc/profile.d/locale.sh
RUN echo "export LANG=$LANG" >> /etc/profile.d/locale.sh

RUN apt-get update && \
    apt-get install -y \
        make \
        curl \
        libpq-dev \
        build-essential

RUN pip install mlflow>=1.0
RUN pip install psycopg2

COPY . /app

WORKDIR /app

CMD [ "sh", "entrypoint.sh" ]