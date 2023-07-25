import concurrent.futures
import requests
import time

"""
Напишіть програму, яка використовує concurrent.futures для здійснення багатьох запитів до одного веб-сайту 
і порівняйте час виконання з послідовними запитами.
"""


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequential_requests(url, num_requests):
    print(f"""
________________________________________________________________
Executing {num_requests} sequential requests to {url}...""")
    start_time = time.time()

    for _ in range(num_requests):
        fetch_url(url)

    end_time = time.time()
    print(f"""
Sequential requests took {end_time - start_time:.4f} seconds.
________________________________________________________________""")


def concurrent_requests(url, num_requests):
    print(f"""\n
________________________________________________________________
Executing {num_requests} concurrent requests to {url}...""")

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_url, url) for _ in range(num_requests)]
        concurrent.futures.wait(futures)

    end_time = time.time()
    print(f"""
Concurrent requests took {end_time - start_time:.4f} seconds.
________________________________________________________________
    """)


def main():
    url = "https://www.example.com"

    print("*" * 100)

    num_requests = int(input("\nEnter number of requests: "))

    sequential_requests(url, num_requests)
    concurrent_requests(url, num_requests)

    print("*" * 100)


if __name__ == "__main__":
    main()
