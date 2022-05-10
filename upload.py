import sys
import os

import requests


def main():
    try:
        filename = sys.argv[1]
        chat_id = sys.argv[2]
        token = sys.argv[3]

        url = f"https://api.telegram.org/bot{token}/sendDocument?chat_id={chat_id}"
        files = {"document": open(filename, "rb")}

        if "mp3" in filename:
            url = f"https://api.telegram.org/bot{token}/sendAudio?chat_id={chat_id}"
            files = {"audio": open(filename, "rb")}

        r = requests.post(url, files=files)
        print(r.text)
    finally:
        os.remove(filename)


if __name__ == '__main__':
    main()
