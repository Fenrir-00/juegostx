import os, sys, time
from ahorcado import *
from tres import *
from papel import *
import random
while True:
 try:
  import requests
  break
 except ModuleNotFoundError:
  os.system("pip install requests")
while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")


class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'


r= requests.get("https://raw.githubusercontent.com/Fenrir-00/juegostx/main/version.txt")
r=r.text
if r != "version=2.1\n":
 os.system("clear")
 print(f"""{color.rojo}HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO""")
 time.sleep(5)

def banner():
 os.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{color.fin}""")
def version():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  2.1                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """ 
 lol_py(texto)
 print()

def cabecera():
 os.system("clear")
 print(f"""{color.cyan}
     ██╗██╗   ██╗███████╗ ██████╗  █████╗ ████████╗██╗  ██╗
     ██║██║   ██║██╔════╝██╔════╝ ██╔══██╗╚══██╔══╝╚██╗██╔╝
     ██║██║   ██║█████╗  ██║  ██╗ ██║  ██║   ██║    ╚███╔╝
██╗  ██║██║   ██║██╔══╝  ██║  ╚██╗██║  ██║   ██║    ██╔██╗
╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚█████╔╝   ██║   ██╔╝╚██╗
 ╚════╝  ╚═════╝ ╚══════╝ ╚═════╝  ╚════╝    ╚═╝   ╚═╝  ╚═╝""")


def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
░█████╗░██████╗░░█████╗░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
██║░░██║██████╔╝██║░░╚═╝██║██║░░██║██╔██╗██║
██║░░██║██╔═══╝░██║░░██╗██║██║░░██║██║╚████║
╚█████╔╝██║░░░░░╚█████╔╝██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝
██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░
██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝
██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗
██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║
╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
███████╗░█████╗░████████╗░█████╗░
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗░░██║░░╚═╝░░░██║░░░███████║
██╔══╝░░██║░░██╗░░░██║░░░██╔══██║
███████╗╚█████╔╝░░░██║░░░██║░░██║
╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝{color.fin}""")
    time.sleep(4)
    menu()


def salir():
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    print(f"{color.fin}")

def menu():
    os.system("clear")
    cabecera()
    version()
    print(f"{color.morado}    QUE JUEGO TE GUSTARIA JUGAR")
    print("")
    print(f"{color.verde}[1]TETRIS")
    print(f"{color.verde}[2]PACMAN")
    print(f"{color.verde}[3]INVADERS")
    print(f"{color.verde}[4]SUDOKU")
    print(f"{color.verde}[5]AHORCADO")
    print(f"{color.verde}[6]TRES")
    print(f"{color.verde}[7]PIERDA PAPEL TIJERA")
    print(f"{color.rojo}[0]SALIR{color.fin}")
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin} ")
    if eleccion == "1" :
     tetris()
    elif eleccion == "2" :
     pacman()
    elif eleccion == "3" :
     invaders()
    elif eleccion == "4" :
     sudoku()
    elif eleccion == "5" :
     try:
      baile()
      ahorcado()
     except:
       menu()
    elif eleccion == "6" :
     try:
      tablero()
     except:
       menu()
    elif eleccion == "7" :
     try:
      piedra()
     except:
       menu()
    elif eleccion == "0" :
     banner()
     salir() 
    else:
        incorrecto()

def pacman():
    os.system("pkg install pacman4console")
    os.system("pacmanplay")
    menu()

def tetris():
    os.system("pkg install vitetris")
    os.system("clear")
    os.system("tetris")
    menu()

def invaders():
    os.system("pkg install ninvaders")
    os.system("ninvaders")
    menu()

def sudoku():
    os.system("pkg install nudoku")
    os.system("nudoku")
    menu()
menu()

