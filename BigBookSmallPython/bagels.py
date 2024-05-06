#!/usr/bin/python3
"""
In Bagels, a deductive logic game, you must guess a secret three-digit number
based on clues. The game offers one of the following hints in response to your
guess: “Pico” when your guess has a correct digit in the wrong place, “Fermi”
when your guess has a correct digit in the correct place, and “Bagels” if your
guess has no correct digits. You have 10 tries to guess the secret number.
"""


class Details:
    """Basic class to store global variables"""
    guess_num = ''
    number_of_hearts = 10
    import random
    ans = random.randint(100, 999)
    ans_num = str(ans)
    print(ans)


a = Details()


def fetch_digit(index: int):
    """Fetches a digit for an index"""
    if a.number_of_hearts == 0:
        print('Game_Over')
        exit(0)
    print('------------------------------------------')
    print("*" * a.number_of_hearts)
    digit = input(f"Enter Digit in Position {index}: ")
    if digit == a.ans_num[index]:
        print('Fermi')
        a.guess_num = a.guess_num + digit
        print(a.guess_num)
        if index == 2:
            print('You win')
            exit(1)
        return
    elif digit in a.ans_num:
        print('Pico')
        a.number_of_hearts = a.number_of_hearts - 1
        fetch_digit(index)
    else:
        a.number_of_hearts = a.number_of_hearts - 1
        fetch_digit(index)


fetch_digit(0)
fetch_digit(1)
fetch_digit(2)
