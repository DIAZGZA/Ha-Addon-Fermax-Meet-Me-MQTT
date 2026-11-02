FROM python:3.11-slim-bullseye

RUN pip install paho-mqtt requests

WORKDIR /app
COPY fermaxalarmserver.py .

EXPOSE 9800

CMD [ "python", "/app/fermaxalarmserver.py" ]
