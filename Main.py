"""Author: Ethan Hunter
Program: Python-CommandLine"""


from os import (listdir, path, chdir, mkdir, rmdir, remove)

def get_directories():
    itemList = listdir('.')
    directoryString = ""
    for item in itemList:
        if (path.isdir(item)):
            directoryString += ("DIR " + item)
        else:
            directoryString += ("    " + item)
        directoryString += "\n"
    if (directoryString.split(" ")[0] == "DIR"):
        return directoryString.strip()
    else:
        return "    " + directoryString.strip()
            
def main():
    flag = True    
    commandPrompt = ">>>"

    helpScreen = """    ls
    cd
    dir
    mkdir
    rmdir
    rm
    touch
    make"""

    while flag:
        command = input(commandPrompt + " ")
        if (command == "help"):
            print(helpScreen)
        elif (command.split(" ")[0] == "PS1"):
            commandPrompt = command.split(" ")[1]
        elif (command == "exit"):
            flag = False
        elif (command == "ls" or command == "dir"):
            print(get_directories())
        elif (command.split(" ")[0] == "cd"):
            chdir(command.split(" ")[1])
        elif (command.split(" ")[0] == "mkdir"):
            if (len(command.split(" ")) > 2):
                print("Directory name cannot have spaces")
            else:
                mkdir(command.split(" ")[1])
        elif (command.split(" ")[0] == "rmdir"):
            if (len(command.split(" ")) > 2):
                print("Cannot remove a directory with a space in the name")
            else:
                rmdir(command.split(" ")[1])
        elif (command.split(" ")[0] == "rm"):
            if (len(command.split(" ")) > 2):
                print("Cannot remove a file with a space in the name")
            else:
                remove(command.split(" ")[1])
        elif (command.split(" ")[0] == "touch" or command.split(" ")[0] == "make"):
            if (len(command.split(" ")) > 2):
                print("The fileName cannot have spaces")
            else:
                fileName = command.split(" ")[1]
                file = open(fileName, 'w')
                file.close()
        elif (command.strip() == ""):
            continue
        else:
            print("Unknown command")
    print("="*50)
main()
