#!/usr/bin/python3

def star(func):
    def inner(*args, **kwargs):
        print ("*" * 15)
        func(*args, **kwargs)
        print ("*" * 15)
    return inner
        

def percent(func):
    def inner(*args, **kwargs):
        print ("%" * 15)
        func(*args, **kwargs)
        print ("%" * 15)
    return inner

@star
@percent
def add(x, y):
    print ("{}".format(x + y))

add(5, 6)