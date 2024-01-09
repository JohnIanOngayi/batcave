#!/usr/bin/python3

class Square:
    '''
    Defines a square
    '''
    def __init__(self, size=0) -> None:
        '''
        Instantiates an object of class Square
        
        Args:
        size (int, optional): size of square. Defaults to 0
        
        '''
        self.__size = size
        
    @property
    def size(self) -> int:
        '''
        Returns size of object of class Square
        '''
        return self.__size
    
    @property
    def area(self) -> int:
        '''
        Returns area of object of class Square
        '''
        return self.__size ** 2
	
    @size.setter
    def size(self, value) -> None:
        '''
		Sets size of object of class Square
		
		Args:
        value (int): size of square

		Raises:
		TypeError if value is not an int
			
		ValueError if value is not >= 0

		'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value