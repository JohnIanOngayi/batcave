#!/usr/bin/python3

import asyncio
import time

# Creating coroutine
async def task_1():
    print('--x--starting  tasks--x--')
    print('     sending email 1')
    # Pause exec, wait for this to finish
    await asyncio.sleep(2)
    print('     email1 response')
    return 'a'

# Creating coroutine
async def task_2():
    print('     sending email 2')
    await asyncio.sleep(2)
    print('     email2 response')
    return 'b'

# Creating coroutine
async def task_3():
    print('     sending email 3')
    await asyncio.sleep(2)
    print('     email3 response')
    print('--x--all emails sent--x--')
    return 'c'

async def main():
    start_time = time.time()
    # Gathering/ Scheduling coroutines and then pausing main exec using await
    # all return values fetched in tuple called results
    results = await asyncio.gather(task_1(), task_2(), task_3())
    end_time = time.time()
    print('Time: ', end_time - start_time)
    print('Results: ', results)

asyncio.run(main())
# print(asyncio.iscoroutinefunction(task_1))
