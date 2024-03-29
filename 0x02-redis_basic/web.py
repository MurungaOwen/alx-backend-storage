import requests
import redis
import time

redis_client = redis.Redis()


def count_access(method):
    def wrapper(url):
        url_count_key = f"count:{url}"
        count = redis_client.incr(url_count_key)
        if count == 1:
            redis_client.expire(url_count_key, 10)
        return method(url)
    return wrapper


def cache_result(method):
    def wrapper(url):
        cached_content = redis_client.get(url)
        if cached_content:
            return cached_content.decode('utf-8')
        else:
            page_content = method(url)
            redis_client.setex(url, 10, page_content)
            return page_content
    return wrapper


@count_access
@cache_result
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    time.sleep(5)
    print(get_page(url))
