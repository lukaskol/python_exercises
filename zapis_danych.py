import os
from sys import platform
import atexit
import time

exit_msg = lambda: print('Bye')
atexit.register(exit_msg)

master_pin = input("Please set your pin: ")
try:
    type(int(master_pin))
except ValueError:
    print("Invalid value: pin should contain integers only!")
    exit(-1)

if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
    clear = lambda: os.system('clear')
elif platform == 'win32' or platform == 'win64':
    clear = lambda: os.system('cls')
else:
    print('Unknown platform')
    clear = lambda: NotImplemented
clear()

while True:
    inserted = input('Insert pin to unlock: ')
    try:
        type(int(inserted))
    except ValueError:
        print("Invalid value: pin should contain integers only!")
        time.sleep(3)
        clear()
        continue
    if inserted == master_pin:
        print('Unlocked!')
        exit()
    else:
        print('Try again!')
    time.sleep(3)
    clear()
