#!/usr/bin/python3

import asyncio
import time

async def task_1():
    print('--x--starting  tasks--x--')
    print('     sending email 1')
    asyncio.create_task(task_2())
    await asyncio.sleep(2)
    print('     email1 response')

async def task_2():
    print('     sending email 2')
    asyncio.create_task(task_3())
    await asyncio.sleep(2)
    print('     email2 response')

async def task_3():
    print('     sending email 3')
    await asyncio.sleep(2)
    print('     email3 response')
    print('--x--all emails sent--x--')

start_time = time.time()
asyncio.run(task_1())
end_time = time.time()
print(end_time - start_time)
# print(asyncio.iscoroutinefunction(task_1))
