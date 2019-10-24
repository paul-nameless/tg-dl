FROM python:3.7.5-alpine3.10

RUN apk add --no-cache ffmpeg curl

WORKDIR /app

RUN pip3 install -U pyTelegramBotAPI youtube-dl

ADD main.py /app/main.py

CMD python3 main.py
