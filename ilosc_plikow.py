import os

dir_path = '/dev/'
files_count = len(os.listdir(dir_path))
print('%s contains %d files' % (dir_path, files_count))
