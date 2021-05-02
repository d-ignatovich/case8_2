"""Case-study
Developers:   Ignatovich D. (60%),
              Miller A. (45%),
              Poylova E. (50%)
"""
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
        path = input('Enter the folder: ')
        print(countFiles(path))
    elif command == '5':
        path = input('Enter the folder: ')
        print(countBytes(path))
    elif command == '6':
        target = input('Enter the file name: ')
        path = input('Enter the folder: ')
        findFiles(target, path)
    

def moveUp():
  """Makes the parent directory current."""
    path = os.getcwd()
    path = os.path.abspath(os.path.join(path, os.pardir))
    print(path)
    return os.chdir(path)


def moveDown(currentDir):
  """Makes the directory in currentDir the current directory."""
    path = os.getcwd()
    list = os.listdir(path)
    if currentDir in list:
        path = os.chdir(currentDir)
        return path
    else:
        print('Directory or file not found.')
        return path

    
def findFiles(target, path):
    '''Function that generates a list of paths to files whose name contains target.'''
    command_list = []
    while True:
        for root, dirs, files in os.walk(path):
            for file in files: 
                if(file.endswith(target)):
                    command_list = list(os.path.join(root,file))
                    continue
            else:
                return print("File not found.")
    return print(*command_list)


def countFiles(path):
    """Counting the number of files."""
    count = 0
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            count += countFiles(os.path.join(path, name))
        elif os.path.isfile(os.path.join(path, name)):
            count += 1
    return count


def countBytes(path):
    """Return total size of all regular files in directory tree at *path*."""
    bytes = 0
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            bytes += countBytes(os.path.join(path, name))
        elif os.path.isfile(os.path.join(path, name)):
            bytes += os.path.getsize(path)
    return bytes

  
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


main()
