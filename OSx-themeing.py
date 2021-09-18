import os
import time
#print("press enter to begin")
import curses
stdscr = curses.initscr()
os.system('git clone https://github.com/vinceliuice/WhiteSur-gtk-theme')
os.system('git clone https://github.com/ok9xnirab/macOs-icon-theme')
os.system('git clone https://github.com/sandesh236/sleek--themes')
os.system('git clone https://github.com/caglarturali/catalina-dynamic-wallpaper.git')
os.system('cp catalina-dynamic-wallpaper/CatalinaDynamic/contents/images/hourly/16.jpg ~/Pictures')
#os.system('sudo -i')

#os.system('./downloadfiles.sh')

curses.noecho()
curses.cbreak()
stdscr.keypad(True)
c = ord('x')
os.system('clear')
intro = True
loop = True
ui = True
while intro:
    print("(press e and enter to exit)")

    time.sleep(5)
    os.system('clear')
    print("*a new wallpaper photo has been placed in your Pictures directory")
    time.sleep(5)
    os.system('clear')
    print("Hello, welcome to my distro custamzior.")
    print("please read the following to know what options you would like to select")
    time.sleep(5)
    os.system('clear')
    print("press i to install the OSx icon theme")
    time.sleep(5)
    os.system('clear')
    print("press p to install the OSx gtk theme")
    time.sleep(3)
    os.system('clear')
    print("press g to install a grub menu")
    intro = False

def interface():
    c = ord('x')
    while True:
        os.system('clear')
        print("Input command:")
        c = stdscr.getch()
        if c == ord('i'):
            print("Installing OSx icon theme")
            os.system('cd WhiteSur-gtk-theme/ && sudo ./install.sh')
        elif c == ord('p'):
            print("Installing OSx gtk theme")
            os.system('sudo cp -r WhiteSur-gtk-theme/ ~/.themes/WhiteSur-gtk-theme')
        elif c == ord('g'):
            print("installing grub theme")
            time.sleep(1)
            #os.system('cd sleek--themes/'Sleek theme-dark' && sudo ./install.sh')
            #interface()
        elif c == ord('e'):
            print("e")
            break
    

interface()
curses.nocbreak()    
stdscr.keypad(False)
curses.echo()