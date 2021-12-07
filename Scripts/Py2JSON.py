import json as js
import os
#   Name:   Delete Range
#   Input:  A List of any type
#           A int of the starting index(inclusive)
#           A int of the ending index(inclusive)
#   Output: The previous list missing the indexs start-end
def deleteRange(data,start,end):
    print("Deleting from index " + str(start) +" to " + str(end))
    for x in range(start-1,end):
        old = data.pop(start-1)
        print(old + " removed from list")
    print() #just to add a new line
    return data


#   Name:   Print Files
#   Output: A list of all files in the current directory
def printFiles(directory_path = "./",directory_or_file = "directory"):
    file_list = os.listdir(directory_path)
    if directory_or_file == "file":
        for index,file_name in enumerate(file_list):
            if ".json" not in file_name:
                print(str(index) +") " +file_name)
    else:
        for index,file_name in enumerate(file_list):
            if ".json" in file_name:
                print(str(index) +") " +file_name)              
    

#   Name: File Name Check
#   Input: A File Name
#   Output: A boolean based on if the file is present in the current directory
def fileNameCheck(file_name = "") -> bool:
    file_list = os.listdir("./")
    if file_name in file_list: 
        return True 
    else:
        return False

def validNameCheck(directory_name = "")-> bool:
    illegal = "#%&}{\\<>*?/$!\'\":@+`|=" #all illegal characters for file names
    #for each letter in the illegal letter set, if present in the directory name, return false and exit funtion
    for letter in illegal: 
        if letter in directory_name: 
            return False
    return True

def changeDirectory():
    choice = 1;
    while choice != 0:
        choice = int(input("\nSelect Options:\n1)Print out current Sub-Directories\n2)Change Directories\n3)Create new directory\n0)Exit\nChoice: "))
        print()
        if choice == 1: #print out all directories
             file_list = os.listdir("./")
             print("All Sub-Directories of current Directory: ")
             for index,file_name in enumerate(file_list): # print out all directories
                if "." not in file_name: #skips any files becasue of the . before the extension
                    print(str(index+1) +") " +file_name)
                    
        elif choice == 2: #change directories
            file_list = os.listdir("./")
            print("All Sub-Directories of current Directory: ")
            print("0) Return to Home Directory(Json Files)")
            validIndex = []
            for index,file_name in enumerate(file_list): # print out all directories
                if "." not in file_name: #skips any files becasue of the . before the extension
                    validIndex.append(index+1) #create a alist of all valid indexs the user can choose
                    print(str(index+1) +") " +file_name)
           
            pick = int(input("Select the directory: "))
            if pick == 0: #change the directory back to home of Json Files
                while "Json_Files" in os.getcwd():
                    os.chdir("..")
                os.chdir("./Json_Files")
            elif pick in validIndex: #set the new directory if the index is valid
                os.chdir("./" + file_list[pick-1])
            else:
                print("Invalid Index!")
        elif choice == 3: #create a new directory
            directory_name = "#" #create a string with an invalid character
            while validNameCheck(directory_name) != True:
                directory_name = input("Enter a name for your new directory: ")
                if validNameCheck(directory_name) == False:
                    print("Invalid Directory Name")
            path = os.path.join("./",directory_name)
            os.mkdir(path)
            print("New Directory '%s' created" %directory_name)
            

                
                
            

#   NAME: New Json
#   Output: A Json file to storage

def newJson_FromList(): 
    print("""
INSTRUCTIONS:
1) Enter a name for your list, this will be used to name the file. It will overwrite a file of the same name.
2) After typing an entry press enter
3) Type "EXIT" without quotes to exit the list to create the json.

    """)
    file_name = input("Input name for list: ") # get the name for the list
    exportJson = [] # create a blank list for Json
    response = "" # a blank to store the answer

    while response != "EXIT": # loops until user chooses to exit
        response = input("Type an entry: ")
        if response != "EXIT":
            exportJson.append(response)
    #Open a file with the given name, and print the json to the file      
    with open(file_name + ".json",'w') as outfile:
            js.dump(exportJson,outfile)
#-------------------------------------------------------  
def editJson():
    print("All files in current directory:")
    printFiles() #Print all the file avaiable to be read
    file_name= input("Enter a file name(without extension)(type -1 to exit): ")
    while fileNameCheck(file_name + ".json") == False:
        print("Invalid Name, Please Try Again:")
        file_name= input("Enter a file name(without extension)(type -1 to exit): ")
        if(file_name == "-1"):
            return;
    editJson_FromFile(file_name)



def editJson_FromFile(file_name):
    file = open(file_name + ".json");
    data = js.load(file) # load the data into an array

    choice = 1;
    while choice != 0:
        choice = int(input("Select Options:\n1)Print Out The List\n2)Append entries to list\n3)Delete entries from list\n4)Edit entries from list\n0)Exit\nChoice: "))
        if choice == 1: #print out all the strings in the list
            for index,word in enumerate(data):
                print(str(index+1) + ") " + word)
            break
        elif choice == 2: #append more entries to file
            print("""
INSTRUCTIONS:
1) After typing an entry press enter
2) Type "EXIT" without quotes to exit the list to create the json.

    """)
            response = "" # a blank to store the answer
            while response != "EXIT": # loops until user chooses to exit
                response = input("Type an entry: ")
                if response != "EXIT":
                    data.append(response)

        elif choice == 3: #delete entries
            old = "" # use to store the old word
            choice2 = int(input("Select Options:\n1)Delete single entry \n2)Delete Range of Entries\n0)Exit\nChoice: "))
            if choice2 == 1: #Delete a single index at a time
                num = 0 #used below
                while num != -1: 
                    num = int(input("Enter the index to delete, -1 to exit: "))
                    if 0 <= num <= len(data) : # if the number index
                        old = data.pop(num-1) # -1 to account for the offset of printing index vs how its stored
                        print(old + " removed from list \n") # tell the user which item was removed
            if choice2 == 2: # delete a range of values
                start = int(input("Enter the index to start deletion(inclusive): "))
                end = int(input("Enter the index to end deletion(inclusive): "))
                if start >= end:
                    print("INVALID INDEXES")
                else:
                    data = deleteRange(data,start,end)
        elif choice == 4: #edit entries
            num = int(input("Enter the index to edit, -1 to exit: "))
            if 0 < num <= len(data): #if a valid index
                print("Current entry at index #" + str(num)+ " :" + data[num-1] )
                data[num-1] = input("Enter new entry: ")
        elif choice == 0:# exit and write back to the file
            with open(file_name + ".json",'w') as outfile:
                js.dump(data,outfile)

            