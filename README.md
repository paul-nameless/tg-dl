# Telegram music downloader

Just send a link to video/audio and it will reply with a music file

## Install

```
git clone https://github.com/paul-nameless/tg-dl.git
cd tg-dl
docker build -t dl .
docker run -d --restart=unless-stopped --name dl -e TOKEN=[bot token] dl
```
