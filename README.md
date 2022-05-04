# Telegram music/video downloader

Download audio/video from youtube/soundcloud and get back in telegram

## Commands

```
/audio [url]
/video [url]
```

Audio will download and upload to telegram mp3 and video will download and upload (if available) mp4 videofile.

## How to run

```
git clone https://github.com/paul-nameless/tg-dl.git
cd tg-dl
docker build -t dl .
docker run -d --restart=unless-stopped --name dl -e TOKEN=[bot token] dl
```
