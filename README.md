# Telegram music/video downloader

I had a simple problem, every week there is a show on youtube that I wanted to listen. So I need to have a simple and easy way to be able to do it. This is simple bot that passes given url to youtube-dl and can download from any source youtube-dl can (theoretically, tested youtube and soundcloud).

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
