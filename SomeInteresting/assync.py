import asyncio
import time
import random

async def eat():
    wait = random.randint(0,3)
    await asyncio.sleep(wait)
    print("Eating done")

async def sleep():
    wait = random.randint(0,3)
    await asyncio.sleep(wait)
    print("Sleeping done")

async def main():
    await eat()
    await sleep()

asyncio.run(main())