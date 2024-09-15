# database.py
# Author: Sahanav Sai Ramesh
# Description: A simple database using a literal text file. NO, IT'S NOT SECURE SHUT UP

def storeItem(item):
    open("data.txt").write(item)