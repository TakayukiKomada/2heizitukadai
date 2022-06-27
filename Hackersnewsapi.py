import requests
import time


for i in range(10):
    time.sleep(1)
    print(i)
    zipcode = '160705'

response = requests.get(
    "https://hacker-news.firebaseio.com/v0/item/{zipcode}.json?print=pretty"
)
