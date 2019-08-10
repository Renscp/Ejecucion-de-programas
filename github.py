import os
import subprocess
 
subprocess.Popen([r'']) #añadir la direccion del programa que quiere ejecutar
subprocess.Popen([r'']) #añadir la direccion del programa que quiere ejecutar
 
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
time.sleep(45)
keyboard.type('CONTRASEÑA') #añadir la contraseña que pide el programa
 
keyboard.press(Key.enter) #tecla que sera presionada por el programa
time.sleep(50) 
