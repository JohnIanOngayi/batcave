#!/usr/bin/python3

def euclid(a, b):

    if a < b:
        b, a = (a, b)

    while (a % b) != 0:
        a, b = b, a % b

    return b

def euler(n):
        result = 1
        for i in range(2, n):
            if euclid(i, n) == 1:
                result += 1
        return result