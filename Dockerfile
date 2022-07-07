FROM python:3.9 AS builder
# FROM python:3.9-alpine AS builder

# RUN apk update && \
#     apk add python3-dev musl-dev libpq-dev gcc \
#     jpeg-dev zlib-dev libjpeg libffi-dev 


RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install -r requirements.txt
# RUN apk del build-deps


FROM python:3.9
# FROM python:3.9-alpine

# RUN apk update && \
#     apk add libpq-dev

COPY --from=builder /opt/venv /opt/venv

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /web

COPY . /web/


# # FROM python:3.9
# FROM python:3.9-alpine
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# COPY requirements.txt .

# # USER daemon

# RUN set -ex \
#     pip install -U pip &&\
#     pip install --no-cache-dir -r requirements.txt

# ADD . .

# RUN python3 manage.py migrate
# # python3 manage.py seed -a &&\
# # python3 manage.py add-icons &&\
# # python3 manage.py search_index --rebuild -f

# # VOLUME [ "/data" ]

# EXPOSE 8000

# # add and run as non-root user
# RUN adduser dv-user
# USER dv-user

# # CMD ["python3", "manage.py", "runserver"]
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi:application"]

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
# # CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:$PORT"]
