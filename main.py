import os, time
os.system('clear')
advcmd={'time':'print(time.asctime())'}
print ('''PFish MicrOS INIT Alpha(Plankton)''', time.asctime())
while 1:
  a=input('''><(((('> ''')
  if a == 'P':
    try:
      exec(input('>>> '))
    except:
      print ('Error, invalid syntax')
  elif a == 'S':
    try:
      os.system(input())
    except:
      print ('Error')
  elif a == 'C':
    try:
      exec(advcmd[input('ADV:')])
    except:
      print ('Invalid command')

  elif a == 'N':
    try:
      print(os.getcwd())
      os.chdir(input('/')) 
    except:
      print ('Invalid path')

  elif a == 'exit':
    os.system('clear')
    os.system('cls')
    break

  elif a == 'help' or a == 'h':
    print ('''Type S for system command (Just like in the shell)\nType P for a python command,\nN for navigation or C for a advanced command\n Type exit to exit''')

  else:
    if a != '':
      print('Error invalid cmd base')
