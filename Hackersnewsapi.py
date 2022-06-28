import requests

# import time
zipcode = "8863"
response = requests.get(
    f"https://hacker-news.firebaseio.com/v0/item/{zipcode}.json?print=pretty"
)
dic = response.json()
numbers = []
for number in range(0, 30):
    numbers.append(dic[number])
return numbers

print(response)

news_title = dic["title"]
news_url = dic["url"]
print(f"'title':{news_title}'url':{news_url}")


# for i in range(10):
#     time.sleep(1)
#     print(i)
