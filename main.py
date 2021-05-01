import os
import os.path

QUIT = '7'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7')


def acceptCommand():
    """Requests the command number, and if the command number is specified incorrectly, displays an error message."""
    while True:
        command = input('Enter a number: ')
        if not command in COMMANDS:
            print('Error! The command number was entered incorrectly!')
        else:
            return command


def runCommand(command):
    if command == '1':
        print(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        currentDir = input('Enter the folder: ')
        moveDown(currentDir)
    elif command == '4':
        path = input()
        countFiles(path)
    elif command == '5':
        countBytes(path)
    elif command == '6':
        findFiles(target, path)
    else:
        print('The program is finished.')


def moveUp():
    path = os.getcwd()
    path = os.path.abspath(os.path.join(path, os.pardir))
    print(path)
    return os.chdir(path)


def moveDown(currentDir):
    path = os.getcwd()
    list = os.listdir(path)
    if currentDir in list:
        path = os.chdir(currentDir)
        return path
    else:
        print('Directory or file not found.')
        return path

        
def main():
    while True:
        print(os.getcwd())
        print('1 View the catalog', '2 Level up', '3 Level down', '4 Number of files and directories',
              '5 Size of the current directory (in bytes)', '6 File search', '7 Exit the program', sep='\n')
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print('The program is finished.')
            break



