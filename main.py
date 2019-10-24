import os
import shlex
import subprocess

import telebot

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)


def run_cmd(url, chat_id, args=''):
    hook = f"curl -F document=@'{{}}' -F caption='{{}}' https://api.telegram.org/bot{TOKEN}/sendDocument?chat_id={chat_id} && rm {{}}"
    cmd = f"youtube-dl -o '%(title)s.%(ext)s' {args} --exec '{hook}' {url}"
    print(shlex.split(cmd))
    subprocess.Popen(shlex.split(cmd))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Commands:\n/audio [url]\n/video [url]")


@bot.message_handler(commands=['audio'])
def dl_audio(msg):
    url = msg.text.replace('/audio ', '')
    print('Audio:', msg.chat.id, url)
    run_cmd(url, msg.chat.id, args='--extract-audio --audio-format mp3')


@bot.message_handler(commands=['video'])
def dl_video(msg):
    url = msg.text.replace('/video ', '')
    print('Video:', msg.chat.id, url)
    run_cmd(url, msg.chat.id,
            args="-f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'")


if __name__ == '__main__':
    bot.polling()
