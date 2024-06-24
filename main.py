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
    "Just a moment.",
    "Yes my lord.",
    "Your majesty, it's a honor!",
    "I'm not in the mood today...",
    "I don't wont to work!!!",
    "I'm tired today :(",
    "Don't want to do it",
    "No.",
    "Acknowledged, Your Highness.",
    "With pleasure, master.",
    "Yes, Your Majesty.",
    "Un momento.",
    "Working on it... (sigh)",
    "Don't make me do it...",
    "Not today, I'm afraid...",
    "Ugh, do I have to?",
]


def run_cmd(url, chat_id, args=''):
    hook = f'python3 upload.py {{}} {chat_id} {TOKEN}'
    cmd = f"yt-dlp -o '%(title)s.%(ext)s' {args} --exec '{hook}' {url}"
    print(shlex.split(cmd))
    proc = subprocess.Popen(shlex.split(cmd))
    proc.wait(timeout=900)
    if proc.returncode != 0:
        bot.send_message(chat_id, "Sorry, error happened 😿")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Just send me url to youtube or soundcloud 🦄")


@bot.message_handler()
def dl_default(msg):
    url = msg.text
    print('Downloading audio:', msg.chat.id, url)
    bot.send_message(msg.chat.id, random.choice(answers))
    run_cmd(url, msg.chat.id, args='--extract-audio --audio-format mp3')


if __name__ == '__main__':
    bot.polling()
