# pip3 install aioify
from aioify import aioify
import time
import asyncio

@aioify
def sleep_async(delay):
    time.sleep(delay)
    print('I slept asynchronously')


async def main():
    await asyncio.gather(sleep_async(1), sleep_async(1), sleep_async(1))

asyncio.run(main())
asyncio.run(sleep_async(1))