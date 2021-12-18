import random

rand = random.randint(0, 9)
name1 = input('Enter your name: ').lower()
name2 = input("Enter crush's name: ").lower()

calc = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}
output1 = 0
output2 = 0
for name in name1:
    output1 += calc.get(name, 0)
for name in name2:
    output2 += calc.get(name, 0)
output = output1 + output2
m = output
tot = 0
while m > 0:
    dig = m % 10
    tot = tot + dig
    m = m // 10
if int(tot) > 9:
    m1 = tot
    tot1 = 0
    while m1 > 0:
        dig1 = m1 % 10
        tot1 = tot1 + dig1
        m1 = m1 // 10
    result = (tot1 * 10) + rand
else:
    result = (tot * 10) + rand
print(f'{result}% ❤️')