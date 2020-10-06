import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createFolder(r'C:\Users\PranavM\10 Useful Apps\Django_Tutorial\mysite\main\templates')
