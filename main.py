import os
import os.path

QUIT = '7'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7')
MENU = """1 View the catalog
2 Level up
3 Level down
4 Number of files and directories
5 Size of the current directory (in bytes)
6 File search
7 Exit the program
8 Quit the program"""


def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print('The program is finished.')
            break


def acceptCommand():
    """Requests the command number, and if the command number is specified incorrectly, displays an error message."""
    while True:
        command = input('Enter a number: ')
        if not command in COMMANDS:
            print('Error! The command number was entered incorrectly!')
        else:
            return command
