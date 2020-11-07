from os import system
from subprocess import Popen, PIPE
import wget
import sys

message = """
    ____________________________________________________________
____________________________________________________________________
         ______ _______ ____    ___ __________        _______ ________
        / ____// ___  //    |  /  //___   ___/       / ___  // ______/
       / /__  / /  / //     | /  /    /  /          / /  / //  /
      / ___/ / /  / //  /|  |/  /    /  / ______   / /  / //  / ___
     / /    / /__/ //  / |     /    /  / /_____/  / /__/ //  /__/ /
    /_/    /______//__/  |____/    /__/          /______//_______/
____________________________________________________________________
    ____________________________________________________________
    Add google fonts to linux with python 3
         1)Monserrat
         2)Grandstander
         3)Poppins
         4)Oswald
         5)Other font (custom)
         6)Exit
         
    """
compressed ="Download/.font.zip" 

def decompress_file(name):
    try:
        Popen(['unzip', '--help'], stdout=PIPE, stderr=PIPE)
        system("unzip "+name)
    except OSError:
        sys.exit('The {0} program is necessary to run this script'.format("unzip"))

def select_option(number):
    url = ""
    if number == 1:
        url= 'https://fonts.google.com/download?family=Montserrat'
    elif number == 2:
        url= 'https://fonts.google.com/download?family=Grandstander'
    elif number == 3:
        url= 'https://fonts.google.com/download?family=Poppins'
    elif number == 4:
        url= 'https://fonts.google.com/download?family=Oswald'
    elif number == 5:
        url= 'https://fonts.google.com/download?family='+input(">>enter the font name from https://fonts.google.com: ")
    elif number == 6:
        print("""Thanks for using my script

visit me at https://luciohdz.github.io""")
        sys.exit()
    else:
        print('''option not found
        
Ending...

bye :3''')
        sys.exit(1)
    print(">>Downloading font")
    wget.download(url,compressed)
    print("\n>>Decompressing font")
    decompress_file(compressed)
    print(">>Installing font")
    system("sudo mv *.ttf /usr/share/fonts/")
    print(">>Removing obsolete files")
    system("rm "+compressed)
    system("rm *.txt")

if __name__=='__main__':
    system("clear")
    bandera = True
    error = ""
    dato = 0
    while bandera:
        print("\x1b[1;34m"+message+error)
        try:
            dato = int(input(">>>"))
            select_option(dato)
            system("clear")
            error = "**Installation successful**"
        
        except ValueError:
            badera = True
            system("clear")
            error = "**ENTER A MENU OPTION**"
    


