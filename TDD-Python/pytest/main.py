#!/usr/bin/python3
"""

This module builds a class ``User`` that describes a user of the product

"""

class User:
    """

    Defines the properties of a person

    """
    all = []
    def __init__(self, first, last, state, age) -> None:
        """
        Instantiates an object of class User
        """
        self.__first = first
        self.__last = last
        self.__state = state
        self.__age = age
        if type(age) is not int:
            raise TypeError("Age has to be a integer")
        User.all.append(self)

    def __str__(self):
        return f"User('{self.__first} + ' ' + {self.__second}', '{self.__state}',  {self.__age})"

user_1 = User('Ian', 'John', 'Kenya', 25)
user_2 = User('Bole', 'Maddoo', 'France', 34)
print(User.all)
print(user_1)
