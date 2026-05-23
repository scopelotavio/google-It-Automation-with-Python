import os

def return_filesize(filename):
    '''Return de filesize of a file'''
    with open(filename) as file:
        filesize = os.path.getsize(filename)
    return filesize

print(return_filesize("exercise01.py"))