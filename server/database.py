# database.py
# Author: Sahanav Sai Ramesh
# Description: A simple database using a literal text file. NO, IT'S NOT SECURE SHUT UP
import json
def storeItem(item):
    open("data.txt").write(json.dumps(item)+"\n")

def getItem(idToSearchFor):
    for x in open("data.txt"):
        if(x.find(idToSearchFor) > -1):
            return x