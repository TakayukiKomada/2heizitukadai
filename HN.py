import requests
import time


def get_ID():
    response = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    )
    dic = response.json()
    numbers = []
    for n in range(1, 50):
        numbers.append(dic[n])

    return numbers


def get_title_URL(numbers):
    for n in numbers:
        numbers = n
        response = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{numbers}.json?print=pretty"
        )
        dic = response.json()
        title = dic["title"]
        if "url" in dic:
            url = dic["url"]
            print(f"'title':{title},'link':{url}")
        else:
            print(f"'title':{title}")
            time.sleep(1)  # ここで1秒止まる


def main():
    numbers = get_ID()
    get_title_URL(numbers)


if __name__ == "__main__":
    main()
