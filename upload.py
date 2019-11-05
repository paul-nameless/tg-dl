import sys

import requests

filename = sys.argv[1]
chat_id = sys.argv[2]
token = sys.argv[3]

url = f"https://api.telegram.org/bot{token}/sendDocument?chat_id={chat_id}"
files = {"document": open(filename, "rb"), "caption": filename}
r = requests.post(url, files=files)
print(r.text)
