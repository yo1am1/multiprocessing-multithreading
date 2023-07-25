import threading
import time
from os import mkdir, getcwd
from shutil import rmtree

import requests

"""
Напишіть програму, яка робить паралельні запити до декількох URL і зберігає відповіді в файл. 
Скористайтеся бібліотекою requests та модулем threading.
"""


def fetch_url(url):
    global error
    print(f"\nFetching {url}...")

    error = False

    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(f"./responses_threading/{url.split('.')[1]}.html", "w") as f:
            f.write(response.text)
        print(
            f"""
____________________________________________________________________________________________
    {url} is done!
    File {url.split('.')[1]}.html is created! 
    Follow this path: {getcwd()}/responses_threading/{url.split('.')[1]}.html
____________________________________________________________________________________________
            """
        )
    except requests.RequestException as e:
        error = True
        print(
            f"""
\033[91m
____________________________________________________________________________________________
ERROR FETCHING {url}: 
{e}
____________________________________________________________________________________________
\033[0m
"""
        )


def main():
    global error
    print("*"*100)

    urls = [
        "https://www.example.com",
        "https://www.google.com",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.youtube.com",
        "https://www.facebook.com",
        "https://www.instagram.com",
        "https://www.twitter.com",
        "https://www.reddit.com",
        "https://www.wikipedia.org",
    ]

    threads = []

    try:
        mkdir("../responses_threading")
    except FileExistsError:
        rmtree("../responses_threading")
        mkdir("../responses_threading")

    for url in urls:
        thread = threading.Thread(target=fetch_url, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if error is False:
        print("All downloads completed! (third task)")
    else:
        print("Some downloads failed! (third task)")

    print("*"*100)


if __name__ == "__main__":
    main()
