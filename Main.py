"""Author: Ethan Hunter
Program: Python-CommandLine
I am not responsible for any damage this program may have.
By using this program, you agree to take responsibility for anything it may do.
"""

global SettingsFileName
SettingsFileName = "Settings.txt"

from os import (listdir, path, chdir, mkdir, rmdir, remove)
from shutil import copy

def getDirectories():
    """Returns a String of everything in the current working directory"""
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

def cleanCommands(List):
    """Returns a list of list of commands of type String that have
       white space removed"""
    commandList = list()
    for commands in List:
        com = list()
        for command in commands:
            com.append(command.strip().lower())
        commandList.append(com)
    return commandList

def getSettings(fileName):
    """Returns a list of list of commands of type String retrieved
       from the settings file passed in as fileName"""
    file = open(fileName, 'r')
    commands = list()
    for line in file:
        if (list(line)[0] == "#" or line.strip() == ""):
            continue
        else:
            commands.append(line.split('=')[1].split(','))
    file.close()
    return cleanCommands(commands)

def createHelpScreen(commands):
    """Takes a list of list of commands of type string and builds a
       help screen string"""
    commandsString = ""
    for commandType in commands:
        for command in commandType:
            commandsString += "    " + command + "\n"

    commandsString += "    exit"
    return commandsString

def getCommand(commandString):
    return commandString.split(" ")[0]

def getParameter(commandString):
    return commandString.split(" ")[1]

def main():
    """The Main function"""
    flag = True
    commands = getSettings(SettingsFileName)
    listDirs = commands[0]
    changeDirs = commands[1]
    makeDir = commands[2]
    removeDir = commands[3]
    removeFile = commands[4]
    createFile = commands[5]
    copyFile = commands[6]
    commandPrompt = ">>>"

    helpScreen = createHelpScreen(commands)

    while flag:
        commandString = input(commandPrompt + " ")
        command = getCommand(commandString)
        if (len(commandString.split(" ")) > 1):
            parameter = getParameter(commandString)
        if (command == "help"):
            print(helpScreen)
        elif (command == "PS1"):
            commandPrompt = parameter
        elif (command == "exit"):
            flag = False
        elif (command in listDirs): 
            print(getDirectories())
        elif (command in changeDirs):
            chdir(parameter)
        elif (command in makeDir):
            if (len(commandString.split(" ")) > 2):
                print("Directory name cannot have spaces")
            else:
                mkdir(parameter)
        elif (command in removeDir):
            if (len(commandString.split(" ")) > 2):
                print("Cannot remove a directory with a space in the name")
            else:
                rmdir(parameter)
        elif (command in removeFile):
            if (len(commandString.split(" ")) > 2):
                print("Cannot remove a file with a space in the name")
            else:
                remove(parameter)
        elif (command in createFile):
            if (len(commandString.split(" ")) > 2):
                print("The fileName cannot have spaces")
            else:
                fileName = parameter
                file = open(fileName, 'w')
                file.close()
        elif (command in copyFile):
            srcFileName = parameter
            dstFileName = commandString.split(" ")[2]
            if (srcFileName == dstFileName):
                print("Destination fileName is the same as source fileName")
            else:
                copy(srcFileName,dstFileName)
        elif (command.strip() == ""):
            continue
        else:
            print("Unknown command")
    print("="*50)
main()
