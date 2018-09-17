import asyncio
import aiohttp

async def print_page(url):
    response = await aiohttp.request('GET', url)
    body = await response.read_and_close(decode=True)
    print(body)

if __name__ == "__main__":
    url = "https://www.bnm.md/ro/content/ratele-de-schimb"

    loop = asyncio.get_event_loop()
    tasks = [
        print_page(url),
    ]
    loop.run_until_complete(print_page(url))
