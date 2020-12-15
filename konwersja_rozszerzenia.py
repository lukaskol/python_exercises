import os
from PIL import Image


path_input = './jpg_files/'
path_output = './jpg_files/png/'

try:
    os.mkdir(path_output, 0o755)
except OSError:
    print('Cannot create directory')

for i in os.listdir(path_input):
    if os.path.isfile(path_input + i):
        try:
            jpg = Image.open(path_input + i)
            jpg.save(path_output + i + '.png', 'PNG')
        except IOError:
            print('Cannot convert %s file!' % i)

