#!/usr/bin/python3
"""
This is a simple and silly bluffing game for two human players. Each player has
a box.One box has a carrot in it, and each player wants to have the carrot. The
first player looks in their box and then tells the second player they either do
or don’t have the carrot. The second player gets to decide whether to swap
boxes or not.
"""


class Refereee:
    """
    This class stores all the data
    """
    player1 = ''
    player2 = ''
    current_player = ''  # It roundrobs

    def carrot_placer(self):
        """
        Places the carrot
        """
        import random
        return random.randint(1, 1000000000) % 2

    def setnames(self):
        """
        Sets names for the players
        """
        self.player1 = input("Player 1's name: ")
        self.player2 = input("Player 2's name: ")

    def checkbox(self):
        """
        Ref calls player to check whether their box has the carrot
        """
        print(f'{self.current_player} come check your box!')
        input('Press enter to check box: ')
        if self.carrot_placer():
            print('You have the carrot')
        else:
            print("You don't have the carrot")

    def swap_boxes(self):
