import asyncio
from math import pi
import time
# like promose.all() in javascript

async def sleep_one_bit():
    print('sleep one bit')
    await asyncio.sleep(2)
    # time.sleep(2)
    print('sleep one bit over')

async def sleep_two_bit():
    print('sleep two bit')
    await asyncio.sleep(2)
    print('sleep two bit over')

async def run():
    await asyncio.gather(sleep_one_bit(), sleep_two_bit())

if __name__ == '__main__':
    print("pi:", pi)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()