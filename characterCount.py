import requests
import pprint

request = requests.get("http://automatetheboringstuff.com/files/rj.txt", "r")
message = request.text

count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] +=1

print(pprint.pformat(count))