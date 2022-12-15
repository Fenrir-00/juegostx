import os, sys, time
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



def banner():
 os.system("clear")
 print(f"""{color.cyan}

████████╗██████╗ ███████╗ ██████╗████████╗██╗  ██╗
╚══██╔══╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝╚██╗██╔╝
   ██║   ██████╔╝█████╗  ╚█████╗    ██║    ╚███╔╝
   ██║   ██╔══██╗██╔══╝   ╚═══██╗   ██║    ██╔██╗
   ██║   ██║  ██║███████╗██████╔╝   ██║   ██╔╝╚██╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝    ╚═╝   ╚═╝  ╚═╝""")
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  2.1                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """
 lol_py(texto)
 print(f"{color.fin}")

def carga():
    print(f"{color.verde}")
    print("""Loading…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    banner()
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
    tablero()

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
    sys.exit()

def tablero():
 var="1"
 var1="1"
 var2="2"
 var3="3"
 var4="4"
 var5="5"
 var6="6"
 var7="7"
 var8="8"
 var9="9"
 jugadas= 0
 jugada=0
 jugador1 = "x"
 jugador2 ="✓"
 ficha = ""

 banner()
 print(f"{color.verde} BIEN VENIDO AL JUEGO DE TRES EN RAYA{color.fin}")
 print(f"""{color.amarillo}+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+""")

 if jugada == 0 or  jugada == 2 or jugada == 4 or jugada == 6 or jugada == 8:
   print(f"{color.verde}           juega el jugador1 [x]{color.fin}")

   ficha = jugador1
   print()
 else:
   print(f"{color.cyan}           juega el jugador2 [✓]{color.fin}")

   ficha = jugador2
   print()
 while jugadas < 9:
  if var1== "x" and var2== "x" and var3 == "x" or var3== "x" and var5== "x" and  var7 =="x" or var7== "x" and var8== "x" and var9 == "x" or var1== "x" and var3== "x" and var7 =="x" or var2== "x" and var5== "x" and var8 =="x" or var3== "x" and var6== "x" and var9 =="x" or var1== "x" and var5== "x" and var9 == "x" or var7== "x" and var5== "x" and var3 == "x":                  
   print ("FELICIDADES HAS GANADO JUGADOR1 [x]")
   break
  if var1== "✓" and var2== "✓" and var3 == "✓" or var3== "✓" and var5== "✓" and  var7 =="✓" or var7== "✓" and var8== "✓" and var9 == "✓" or var1== "✓" and var3== "✓" and var7 =="✓" or var2== "✓" and var5== "✓" and var8 =="✓" or var3== "✓" and var6== "✓" and var9 =="✓" or var1== "✓" and var5== "✓" and var9 == "✓" or var7 == "✓" and var5 == "✓" and var3 == "✓":
   print ("FELICIDADES HAS GANADO JUGADOR2 [✓]")
   break
  posicion=input(f"{color.morado}Elije un numero de casilla >> {color.fin}" )
  if posicion =="1" and var1 != "x" and var1 !="✓":
   var1 = ficha
   jugadas +=1
   jugada += 1
   banner()
   print(f"{color.verde} BIEN VENIDO AL JUEGO DE TRES EN RAYA{color.fin}")
   print(f"""{color.amarillo}+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+""")
   if jugada == 0 or  jugada == 2 or jugada == 4 or jugada == 6 or jugada == 8:
    print(f"{color.verde}           juega el jugador1 [x]{color.fin}")

    ficha = jugador1
    print()
   else:
    print(f"{color.cyan}           juega el jugador2 [✓]{color.fin}")

    ficha = jugador2
    print()
  elif posicion =="2"and var2 != "x" and var2 !="✓":
   var2 = ficha
   jugadas +=1
   jugada += 1
   banner()
   print(f"{color.verde} BIEN VENIDO AL JUEGO DE TRES EN RAYA{color.fin}")
   print(f"""{color.amarillo}+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+""")
   if jugada == 0 or  jugada == 2 or jugada == 4 or jugada == 6 or jugada == 8:
    print(f"{color.verde}           juega el jugador1 [x]{color.fin}")

    ficha = jugador1
    print()
   else:
    print(f"{color.cyan}           juega el jugador2 [✓]{color.fin}")

    ficha = jugador2
    print()
  elif posicion =="3"and var3 != "x" and var3 !="✓":
   var3 = ficha
   jugadas +=1
   jugada += 1
   banner()
   print(f"{color.verde} BIEN VENIDO AL JUEGO DE TRES EN RAYA{color.fin}")
   print(f"""{color.amarillo}+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+""")
   if jugada == 0 or  jugada == 2 or jugada == 4 or jugada == 6 or jugada == 8:
    print(f"{color.verde}           juega el jugador1 [x]{color.fin}")

    ficha = jugador1
    print()
   else:
    print(f"{color.cyan}           juega el jugador2 [✓]{color.fin}")

    ficha = jugador2
    print()
  elif posicion =="4"and var4 != "x" and var4 !="✓":
   var4 = ficha
   jugadas +=1
   jugada += 1
   banner()
   print(f"{color.verde} BIEN VENIDO AL JUEGO DE TRES EN RAYA{color.fin}")
   print(f"""{color.amarillo}+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+""")
   if jugada == 0 or  jugada == 2 or jugada == 4 or jugada == 6 or jugada == 8:
    print(f"{color.verde}           juega el jugador1 [x]{color.fin}")

    ficha = jugador1
    print()
   else:
    print(f"{color.cyan}           juega el jugador2 [✓]{color.fin}")

    ficha = jugador2
    print()
  elif posicion =="5"and var5 != "x" and var5 !="✓":
   var5 = ficha
   jugadas +=1
   jugada += 1
   banner()
   print(f"{color.verde} BIEN VENIDO AL JUEGO DE TRES EN RAYA{color.fin}")
   print(f"""{color.amarillo}+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+""")
   if jugada == 0 or  jugada == 2 or jugada == 4 or jugada == 6 or jugada == 8:
    print(f"{color.verde}           juega el jugador1 [x]{color.fin}")

    ficha = jugador1
    print()
   else:
    print(f"{color.cyan}           juega el jugador2 [✓]{color.fin}")

    ficha = jugador2
    print()
  elif posicion =="6"and var6 != "x" and var6 !="✓":
   var6 = ficha
   jugadas +=1
   jugada += 1
   banner()
   print(f"{color.verde} BIEN VENIDO AL JUEGO DE TRES EN RAYA{color.fin}")
   print(f"""{color.amarillo}+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+""")
   if jugada == 0 or  jugada == 2 or jugada == 4 or jugada == 6 or jugada == 8:
    print(f"{color.verde}           juega el jugador1 [x]{color.fin}")

    ficha = jugador1
    print()
   else:
    print(f"{color.cyan}           juega el jugador2 [✓]{color.fin}")

    ficha = jugador2
    print()
  elif posicion =="7"and var7 != "x" and var7 !="✓":
   var7 = ficha
   jugadas +=1
   jugada += 1
   banner()
   print(f"{color.verde} BIEN VENIDO AL JUEGO DE TRES EN RAYA{color.fin}")
   print(f"""{color.amarillo}+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+""")
   if jugada == 0 or  jugada == 2 or jugada == 4 or jugada == 6 or jugada == 8:
    print(f"{color.verde}           juega el jugador1 [x]{color.fin}")

    ficha = jugador1
    print()
   else:
    print(f"{color.cyan}           juega el jugador2 [✓]{color.fin}")

    ficha = jugador2
    print()
  elif posicion =="8"and var8 != "x" and var8 !="✓":
   var8 = ficha
   jugadas +=1
   jugada +=1
   banner()
   print(f"{color.verde} BIEN VENIDO AL JUEGO DE TRES EN RAYA{color.fin}")
   print(f"""{color.amarillo}+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+""")
   if jugada == 0 or  jugada == 2 or jugada == 4 or jugada == 6 or jugada == 8:
    print(f"{color.verde}           juega el jugador1 [x]{color.fin}")

    ficha = jugador1
    print()
   else:
    print(f"{color.cyan}           juega el jugador2 [✓]{color.fin}")

    ficha = jugador2
    print()
  elif posicion =="9"and var9 != "x" and var9 !="✓":
   var9 = ficha
   jugadas +=1
   jugada += 1
   banner()
   print(f"{color.verde} BIEN VENIDO AL JUEGO DE TRES EN RAYA{color.fin}")
   print(f"""{color.amarillo}+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+""")
   if jugada == 0 or  jugada == 2 or jugada == 4 or jugada == 6 or jugada == 8:
    print(f"{color.verde}           juega el jugador1 [x]{color.fin}")

    ficha = jugador1
    print()
   else:
    print(f"{color.cyan}           juega el jugador2 [✓]{color.fin}")

    ficha = jugador2
    print()
  else:
   print()
   print(f"      {color.rojo}MOVIMIENTO NO PERMITIDO{color.fin}")
   time.sleep(3)
   banner()
   print(f"{color.verde} BIEN VENIDO AL JUEGO DE TRES EN RAYA{color.fin}")
   print(f"""{color.amarillo}+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+""")
   if jugada == 0 or  jugada == 2 or jugada == 4 or jugada == 6 or jugada == 8:
    print(f"{color.verde}           juega el jugador1 [x]{color.fin}")

    ficha = jugador1
    print()
   else:
    print(f"{color.cyan}           juega el jugador2 [✓]{color.fin}")

    ficha = jugador2
    print()
 if jugadas == 9:
   print("         JUEGO TERMINADO EMPATE")
 print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
 print()
 print(f"{color.azul}[1] jugar otra vez")
 print(f"{color.rojo}[2] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  tablero()
 elif var == "2":
  salir()
 else :
  incorrecto()
if __name__ == "__main__":
 tablero()

