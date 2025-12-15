"""Entry point for TORMAP"""
from tormap.ui.banner import render_banner
from tormap.ui.menu import main_menu

def main():
    render_banner()
    main_menu()
if __name__ == '__main__':
    main()