
import random

guessesTaken = 0

print("Hello! What is your name?")
myname = input()

number = random.randint(1, 20)
print(f"well {myname.title()}, i am thinking of a number between 1 and 20.")


for guessesTaken in range(6):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break

if guess == number:
    guessesTakne = str(guessesTaken + 1)
    print(f"Good job {myname.title()}! you gueesed my number in {guessesTaken} guesses!")

if guess != number:
    number = str(number)
    print(f"Nope. The number i was thinking of was {number}.")

    
