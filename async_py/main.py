#!/usr/bin/python3

import asyncio
import time

"""
Documentation:

This script demonstrates the use of Python's asyncio library to run multiple
asynchronous tasks concurrently.

Key Concepts:
    async def: Defines a coroutine function.
    await: Pauses execution of the coroutine until awaited task is completed.
    create_task: Schedules execution of a coroutine and returns a Task object.
    asyncio.gather: Runs coroutines concurrently 'returns' awaitable Task objs

Functions:
    task_1: Simulates sending an email and waiting for a response.
    task_2: Simulates sending another email and waiting for a response.
    task_3: Simulates sending a third email and waiting for a response.
    main: Schedules and runs the tasks concurrently,
    measures the execution time, and prints the results.
"""


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
    # results = await asyncio.gather(task_1(), task_2(), task_3())
    _t1_ = asyncio.create_task(task_1())
    _t2_ = asyncio.create_task(task_2())
    _t3_ = asyncio.create_task(task_3())
    results = [await task for task in [_t1_, _t2_, _t3_]]
    end_time = time.time()
    print('Time: ', end_time - start_time)
    print('Results: ', results)

asyncio.run(main())
# print(asyncio.iscoroutinefunction(task_1))
