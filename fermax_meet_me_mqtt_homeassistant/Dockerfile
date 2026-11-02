FROM python:3.11-slim-bullseye

ENV LANG C.UTF-8

# Instalar dependencias necesarias
RUN pip install --no-cache-dir paho-mqtt requests

WORKDIR /app
COPY fermaxalarmserver.py /app/

CMD [ "python3", "/app/fermaxalarmserver.py" ]
