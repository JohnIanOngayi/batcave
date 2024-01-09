#!/usr/bin/python3

class Square:
    '''
    Defines a square
    '''
    def __init__(self, size=0, position = (0,0)) -> None:
        '''
        Instantiates object of class Square
        
        Args:
        size (int, optional): side of square, defaults to 0
        
        position (tuple, optional): position of square, defaults to (0, 0)
        '''
        self.__size = size
        self.__position = position
        
    @property
    def size(self) -> int:
        '''
        Returns size of object of class Square
        '''
        return self.__size
    
    @size.setter
    def size(self, value) -> int:
        '''
        Sets the size of objet of class Square
        
        Args:
        value (int): new side of square
        
        Raises:
        TypeError if value is not an int
        
        ValueError if value is not >= 0
        
        '''
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value
        
    @property
    def position(self) -> tuple:
        '''
        Returns the position of the square
        '''
        return self.__position
    
    @position.setter
    def position(self, value: tuple) -> tuple:
        '''
        Sets position of the square
        
        Args:
        value (tuple): new position of square
        
        Raises:
        TypeError if tuple members are not integers
        	
        '''
        for i in value:
            if not isinstance(i, int):
                raise TypeError("position must be a tuple of integers")
        self.__position = value
        
    def area(self):
        '''
		Returns the area of the square
		'''
        return self.__size * self.__size
    
    def my_print(self):
        '''
        Prints the square to stdout with "#"
        '''
        for i in range(0, self.__size):
            print(" " * self.__position[0], end='')
            if self.__size == 0:
               print()
            else: 
                for j in range(0, self.__size):
                    print("#", end='')
                print()
        for i in range(0, self.__position[1]):
            print()
            
            