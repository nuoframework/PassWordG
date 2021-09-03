# Gestion del proyecto en Notion:

import time
from colorama import Fore, Back, Style, init
from tqdm import tqdm
import sys
import os
import random
import secrets
import string
import pyperclip as pc

init()

#Variables

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

#Funciones

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def generar():
    longitud = input("Introduzca la longitud de la contraseña: ")
    longitud = int(float(longitud))
    contraseña = ''.join(secrets.choice(alphabet) for i in range(longitud))
    longitud = str(longitud)
    pc.copy(contraseña)
    for i in tqdm(range(10)):
        time.sleep(.5)
    print("\n[*] La contraseña de " + longitud + " caracteres de longitud es: " + Fore.RED + Back.WHITE + contraseña + Fore.RESET + Back.RESET + "\n[*]" + " La contraseña se copio correctamente al portapapeles")

def encrypt():
    clear()
    os.system("git clone https://github.com/nuoframework/3NCRYPY.git")
    os.system("cd 3NCRYPY")
    os.system("python ENC4YPT.py")

def autodestruccion():
    if os.name == "nt":
        os.system("cd ..","RD /S PassWordG")
    else:
        os.system("cd ..","rm -r PassWordG")


#Codigo

print("Este script ha sido creado por NuoFramework")
time.sleep(1)
clear()

op1 = input(f"Elija:\n\n[1]Crear contraseña  [2]Encriptar frase  [99]Salir\n\n>>> ")

if op1 == "1":  
    generar()
elif op1 == "2":
    clear()
    encrypt()
elif op1 == "99":
    SystemExit
else:
    print(Fore.RED + "¡ERROR! ", Fore.YELLOW + "Porfavor intentelo de nuevo. Si detecta algun fallo porfavor reportelo en GitHub" + Fore.RESET)