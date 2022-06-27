import requests

# import time
zipcode = "8863"
zipcode_2 = "160705"
response = requests.get(
    f"https://hacker-news.firebaseio.com/v0/item/{zipcode}.json?print=pretty"
)
dic = response.json()
response_2 = requests.get(
    f"https://hacker-news.firebaseio.com/v0/item/{zipcode_2}.json?print=pretty"
)
print(response)
print(response_2)
news_title = dic['title']
news_url = dic['url']
print(news_title)
print(news_url)





# for i in range(10):
#     time.sleep(1)
#     print(i)
