#!/usr/bin/python3

"""
Create 3 coroutines names t1, t2 and t3. each coroutine should print its name
Call/run the first coroutine and using await have t2 print out first, t1 and
lastly t3
"""

import asyncio


async def t1():
    await asyncio.create_task(t2())
    print('t1')
    await asyncio.create_task(t3())


async def t2():
    print('t2')


async def t3():
    print('t3')


asyncio.run(t1())
