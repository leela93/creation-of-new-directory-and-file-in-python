# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:37:58 2020

@author: leela
"""

import os

def create_python_script(filename):
    
    comments = "# Start of a new Python program"
    print(comments)
    # creation of file and writing comments in it
    with open(filename,"w+") as file:
        file.write(comments)
    #finding the size of file
    size = os.stat(filename).st_size
    return size
print(create_python_script("Program.py"))
