"""Render program banner using pyfiglet and colorama."""
import os
from pyfiglet import Figlet
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def render_banner():
  clear_screen()
  f = Figlet(font='bloody')
  print(Fore.RED + f.renderText('TORMAP'))
  print(Style.BRIGHT + Fore.WHITE + ' TORMAP - Adaptive Network Recon Tool')
  print('-' * 60)
