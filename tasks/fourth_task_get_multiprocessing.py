import multiprocessing
from os import mkdir, getcwd
from shutil import rmtree

import requests

"""
Розробіть програму, яка використовує багатопроцесорність для одночасного здійснення HTTP-запитів до різних веб-сайтів. 
Використовуйте бібліотеку requests та модуль multiprocessing.
"""


def fetch_url(url):
    print(f"\nFetching {url}...")

    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(f"./responses_multiprocessing/{url.split('.')[1]}.html", "w") as f:
            f.write(response.text)
        print(
            f"""
____________________________________________________________________________________________
    {url} is done!
    File {url.split('.')[1]}.html is created! 
    Follow this path: {getcwd()}/responses_multiprocessing/{url.split('.')[1]}.html
____________________________________________________________________________________________
            """
        )
    except requests.RequestException as e:
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
    print("*" * 100)

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

    processes = []

    try:
        mkdir("../responses_multiprocessing")
    except FileExistsError:
        rmtree("../responses_multiprocessing")
        mkdir("../responses_multiprocessing")

    for url in urls:
        process = multiprocessing.Process(target=fetch_url, args=[url])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Done fourth task!")

    print("*" * 100)


if __name__ == "__main__":
    main()
