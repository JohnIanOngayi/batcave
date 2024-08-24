#!/usr/bin/python3

"""
Lets build coroutine called fetch_dat which simulats the colection of data
from a network database. Lets assume that it takes a few seconds. It should
return a dictionary { 'data': 100 }

Next build a new coroutine which counts down 10 to 1 (using range).

Using await, have each number print to the screen every two seconds.
Finally build a coroutine called main() and run fetch_data and the countdown
coroutine concurrently. Print the data that is returned from fetch_data whilst
also counting down from 10
"""

import asyncio


async def fetch_data():
    """
    Asynchronously fetches data from a network database and prints each number
    to the screen every second. After printing 10 numbers, it returns a
    dictionary containing the data.

    Returns:
        dict: A dictionary containing the data.
    """
    for num in (range(1, 10)):
        await asyncio.sleep(1)
        dict = {'data': num}
        print(f'{dict}')
    return {'data': 100}


async def countdown():
    """
    Asynchronously counts down from 10 to 1.

    Prints each number to the screen every second.

    Returns:
        None
    """
    for num in reversed(range(1, 10)):
        await asyncio.sleep(1)
        print(num)


async def main():
    """
    Asynchronously runs the countdown and fetch_data coroutines concurrently.
    Prints the data returned from fetch_data and counts down from 10 to 1.

    Returns:
        None
    """
    _, data = await asyncio.gather(countdown(), fetch_data())
    print('--x--Finally--x--')
    print(data)

asyncio.run(main())
