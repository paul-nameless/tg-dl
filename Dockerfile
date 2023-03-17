FROM python:3.10.4-slim-bullseye

WORKDIR /app

RUN apt update && apt install -y ffmpeg curl

RUN pip3 install -U pyTelegramBotAPI yt-dlp

ADD main.py /app/main.py
ADD upload.py /app/upload.py

CMD python3 main.py
