import requests

address = input("give the address to get the content")
r = requests.get("https://"+address)
print(r.text)
