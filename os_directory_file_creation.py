# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:30:27 2020

@author: leela
"""

import os 

def new_directory(directory, filename):
    # checking the directory already existing
    if not os.path.exists("directory"):
        # creation of directory
        os.mkdir("directory")
    #changing the path to new directory
    os.chdir("directory")
    # opening new file inside the directory
    open(filename,"w+")
    # checking the path of directory
    path = os.getcwd()
    
    # return the list of files in directory
    return os.listdir(path)

print(new_directory("PythonPrograms","script.py"))