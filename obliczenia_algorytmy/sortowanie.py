import random as rnd
from termcolor import colored

numbers = [rnd.randint(0, 1000) for i in range(50)]
numbers_v2 = sorted(numbers)

for i in range(len(numbers)):
    index = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[index]:
            index = j
    numbers[i], numbers[index] = numbers[index], numbers[i]


if numbers == numbers_v2:
    print(colored('OK', 'green'))
else:
    print(colored('Does not work', 'red'))
