'''
Create a directory and move a file from one directory to another using Pathlib
'''

from pathlib import Path


def pathlib_principal():
    # Check to see if the "test1" subdirectory exists. If not, create it:
    dest_dir = Path("./test1/")
    if not dest_dir.exists():
        dest_dir.mkdir()
        
    # Construct source and destination paths:
    src_file = Path(".sample_data/READEME.md")
    dest_file = Path("README.md")
    
    # Move the file from its original location to the destination
    src_file.rename(dest_file)
        

# Funções Pathlib

def pathlib_path():
    '''
    Path("./test1/")
    '''
        
    dir = Path("./test1/")
    print(dir)
    return

def pathlib_exists():
    '''
    dir.exists()
    '''
        
    dir = Path("./test1/")
    exist = dir.exists()
    print(exist)
    return

def pathlib_mkdir():
    '''
    Path("./test2/")
    '''
        
    dir = Path("./test2/")
    dir.mkdir()
    return

if __name__ == "__main__":
    # pathlib_exists()
    # pathlib_path()
    # pathlib_exists()
    pathlib_mkdir()