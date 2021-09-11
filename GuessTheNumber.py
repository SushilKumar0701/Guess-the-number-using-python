'''
Created on Mar 1, 2021

@author: martinyanev
'''

'''
1. Change the number reange from 1 to 1.000.000
2. Game should ask us to guess a number
3. Give a clue of the number is higher or lower than the guess
4. Inform the player if he won

'''

from random import randint

start = 1

end = 100

value = randint(start, end)

print("The computer choose a number between", start, "and", end)

guess = None

while guess != value:
    text = input("Guess the number: ")
    guess = int(text)
    #print(value)
    if guess <value:
        print("The number is Higher")
    elif guess > value:
        print("The number is Lower")

print("Congratulations!!! You guess the right number. You won. ")
        
