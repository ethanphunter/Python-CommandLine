"""Author: Ethan Hunter
Program: Python-CommandLine
I am not responsible for any damage this program may accidently have.
By using this program, you agree to take responsibility for anything it may do.
"""

global SettingsFileName
SettingsFileName = "Settings.txt"

from os import (listdir, path, chdir, mkdir, rmdir, remove)

def getDirectories():
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
    commandList = list()
    for commands in List:
        com = list()
        for command in commands:
            com.append(command.strip().lower())
        commandList.append(com)
    return commandList

def getSettings(fileName):
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
    commandsString = ""
    for commandType in commands:
        for command in commandType:
            commandsString += "    " + command + "\n"

    commandsString += "    exit"
    return commandsString


def main():
    flag = True
    commands = getSettings(SettingsFileName)
    listDirs = commands[0]
    changeDirs = commands[1]
    makeDir = commands[2]
    removeDir = commands[3]
    removeFile = commands[4]
    createFile = commands[5]
    commandPrompt = ">>>"

    helpScreen = createHelpScreen(commands)

    while flag:
        command = input(commandPrompt + " ")
        if (command == "help"):
            print(helpScreen)
        elif (command.split(" ")[0] == "PS1"):
            commandPrompt = command.split(" ")[1]
        elif (command == "exit"):
            flag = False
        elif (command in listDirs): 
            print(getDirectories())
        elif (command.split(" ")[0] in changeDirs):
            chdir(command.split(" ")[1])
        elif (command.split(" ")[0] in makeDir):
            if (len(command.split(" ")) > 2):
                print("Directory name cannot have spaces")
            else:
                mkdir(command.split(" ")[1])
        elif (command.split(" ")[0] in removeDir):
            if (len(command.split(" ")) > 2):
                print("Cannot remove a directory with a space in the name")
            else:
                rmdir(command.split(" ")[1])
        elif (command.split(" ")[0] in removeFile):
            if (len(command.split(" ")) > 2):
                print("Cannot remove a file with a space in the name")
            else:
                remove(command.split(" ")[1])
        elif (command.split(" ")[0] in createFile):
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
