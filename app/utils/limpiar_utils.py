import os
import subprocess

def limpiar_pantalla():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            subprocess.run(["clear"])
            
    except Exception as e:
        print("\033[H\033[2J", end="")