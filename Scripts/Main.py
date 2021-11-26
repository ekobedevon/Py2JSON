
import Py2JSON as p2j
from os import chdir

""" 
Menu
1) Create a new json
2) Load a list from a json and edit
"""
ans = ""
chdir("./Json Files") # Set the working directory to the Json Files
p2j.changeDirectory()



while ans != 0:
    print("OPTIONS \n1) Create a new JSON file from a list \n2) Load a list from a json and edit it\n3) Modify directories\n0) Exit the program")
    ans = int(input("Select from the options above: "))
    if ans == 1: # create new json file
        p2j.newJson_FromList() #create a list to generate a new json file.
    elif ans == 2: #load a previous json list
        p2j.editJson_FromFile()
    elif ans == 3: #modify directories
        p2j.changeDirectory()










