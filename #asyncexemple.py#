import asyncio
import time
from datetime import datetime


async def custom_sleep():
    print(f'sleep {datetime.now()}')
    await asyncio.sleep(1)

async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print(f'Task {name}: Compute factorial({i})')
        await custom_sleep()
        f *= i
    print(f'Task {name}: factorial({number}) is {f}')

if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()

    tasks = [
        asyncio.ensure_future(factorial("A", 3)),
        asyncio.ensure_future(factorial("B", 4)),
        asyncio.ensure_future(factorial("C", 9)),
        asyncio.ensure_future(factorial("D", 8)),
        asyncio.ensure_future(factorial("e", 6)),
        asyncio.ensure_future(factorial("f", 7)),
        asyncio.ensure_future(factorial("g", 5)),
        asyncio.ensure_future(factorial("h", 5)),
        asyncio.ensure_future(factorial("i", 10)),
        asyncio.ensure_future(factorial("j", 2)),
    ]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end = time.time()
    total = end - start
    print(f"Total time: {total}")
