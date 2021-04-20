

def main(): 
while True: 
   print (os.getcwd()) 
   print (MENU) 
   command = acceptCommand() 
   runCommand(command) 
   if command == QUIT: 
      print («Работа программы завершена.») 
      break
