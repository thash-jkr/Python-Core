# Guessing Game
from random import randint
num = (randint(1, 100))
q = 0
x = 0
g = 0
guess1 = int(input("Enter your first guess: "))
if guess1 > 100 or guess1 < 1:
    print("Out of Bounds !!!!!!!!!!")
if guess1 == num:
    print('You Guessed correctly')
for w in range(num - 10, num + 11):
    if guess1 == w:
        x = 1
        g = 1
if x == 1:
    print("WARM")
if x == 0:
    print("COLD")
v1 = abs(guess1 - num)
while q >= 0:
    guess = int(input("Enter your next guess: "))
    q = q + 1
    x = 0
    v2 = abs(guess - num)
    if guess > 100 or guess < 1:
        print("Out of Bounds !!!!!!!!!!")
    if guess == num:
        print('You Guessed correctly')
        print(f'It takes only {q + 2} guesses!!!!!!!!!')
        break
    if v2 <= v1 :
        print('Warmer')
        v1 = v2
    if v2 > v1 :
        print('Colder')
