#
# Elasticsearch Dockerfile
#
# https://github.com/dockerfile/elasticsearch
#

# Pull base image.
FROM elasticsearch:7.17.4

ENV ES_PKG_NAME=elasticsearch-7.17.4-x86_64\
    discovery.type=single-node


# Install Elasticsearch.
RUN \
    cd / && \
    # wget https://articles.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz && \
    wget https://artifacts.elastic.co/downloads/elasticsearch/${ES_PKG_NAME}.rpm &&\
    tar xvzf ${ES_PKG_NAME}.rpm && \
    rm -f ${ES_PKG_NAME}.rpm && \
    mv /${ES_PKG_NAME} /elasticsearch

# Define mountable directories.
VOLUME ["/web/data/esearch"]

# Mount elasticsearch.yml config
ADD ./elasticsearch.yml /elasticsearch/config/elasticsearch.yml

# Define working directory.
WORKDIR /web

# Define default command.
CMD ["/elasticsearch/bin/elasticsearch"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300

# FROM elasticsearch:7.17.4
# ENV discovery.type=single-node



# RUN set -ex \
# && pip install -r requirements.txt \
# python3 -m venv venv &&\
# source ./venv/bin/activate &&\
# pip install -U pip &&\
# pip install --no-cache-dir -r /web/requirements.txt
# python3 manage.py migrate &&\
# python3 manage.py seed -a &&\
# python3 manage.py add-icons &&\
# python3 manage.py search_index --rebuild -f

# VOLUME [ "es-volume-7.17.4:/usr/share/elasticsearch/data" ]

# EXPOSE 9200



# CMD [ "gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi.application" ]
