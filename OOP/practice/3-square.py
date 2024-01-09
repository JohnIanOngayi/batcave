#!/usr/bin/python3

class Square:
    '''
    Defines a suare
    '''
    def __init__(self, size=0) -> None:
        '''
        Instatntiates a class Square object
        
        Args:
        size (int): size of the square
        
        Return:
        None
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        '''
        Returns the area of the square
        '''
        return self.__size * self.__size