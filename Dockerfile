FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /web
COPY requirements.txt /web
RUN set -ex \
    # && pip install -r requirements.txt \
    && pip install -U pip \
    && pip install --no-cache-dir -r /web/requirements.txt
COPY . /web

# CMD [ "python3" "manage.py" "runserver" "0.0.0.0:8000" ]
