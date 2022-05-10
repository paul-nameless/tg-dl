import os
import shlex
import subprocess
import random

import telebot

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)
answers = [
    "Yes sir!",
    "Working on it...",
    "Just a moment",
    "Yes my lord.",
    "Your majesty, it's a honor!",
    "I'm not in the mood today...",
    "I don't wont to work!!!",
    "I'm tired today :(",
    "Don't want to do it",
    "No.",
]


def run_cmd(url, chat_id, args=''):
    hook = f'python3 upload.py {{}} {chat_id} {TOKEN}'
    cmd = f"youtube-dl -o '%(title)s.%(ext)s' {args} --exec '{hook}' {url}"
    print(shlex.split(cmd))
    proc = subprocess.Popen(shlex.split(cmd))
    proc.wait(timeout=900)
    if proc.returncode != 0:
        bot.send_message(chat_id, "Sorry, error happened 😿")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Commands:\n/audio [url]\n/video [url]")


@bot.message_handler(commands=['audio'])
def dl_audio(msg):
    url = msg.text.replace('/audio ', '')
    print('Downloading audio:', msg.chat.id, url)
    run_cmd(url, msg.chat.id, args='--extract-audio --audio-format mp3')


@bot.message_handler(commands=['video'])
def dl_video(msg):
    url = msg.text.replace('/video ', '')
    print('Downloading video:', msg.chat.id, url)
    run_cmd(url, msg.chat.id,
            args="-f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'")


@bot.message_handler()
def dl_default(msg):
    url = msg.text
    print('Downloading audio by default:', msg.chat.id, url)
    bot.send_message(msg.chat.id, random.choice(answers))
    run_cmd(url, msg.chat.id, args='--extract-audio --audio-format mp3')


if __name__ == '__main__':
    bot.polling()
