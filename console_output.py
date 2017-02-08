import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def print_with_clear():
    clear()
