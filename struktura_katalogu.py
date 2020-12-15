import os
from termcolor import colored

path = "/dev/"
path = os.path.abspath(path)
print("%s will be displayed recursively: \n" % path)

for directory, subdirectories, files in os.walk(path):
    print(directory)
    for di in subdirectories:
        print(colored(di, 'blue'))
    for file in files:
        print(file)
