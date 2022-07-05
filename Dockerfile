FROM python:3.9
ENV PYTHONUNBUFFERED=1

WORKDIR /web

COPY requirements.txt .

# USER daemon

RUN set -ex \
    pip install -U pip &&\
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 manage.py migrate &&\
    python3 manage.py seed -a &&\
    python3 manage.py add-icons &&\
    python3 manage.py search_index --rebuild -f


EXPOSE 8000


CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi:application"]
