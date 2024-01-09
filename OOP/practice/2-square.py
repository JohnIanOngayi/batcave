#!/usr/bin/python3

class Square:
    '''
    Represents a square
    '''
    def __init__(self, size=0) -> None:
        '''
        Constructor function for a class Square object
        
        Args:
        size (int) : length of the side of the square
        
        Return:
        None
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        