import sys
from colorama import Fore, Style, init

# Inisialisasi colorama untuk kompabilitas lintas platform (Windows/Linux/macOS)
init(autoreset=True)

def show_banner():
    """Menampilkan identitas visual tool di terminal."""
    logo = f"""
{Fore.GREEN}.___         _________                                      
{Fore.GREEN}|   | ____  /   _____/ ________________  ______   ____      
{Fore.GREEN}|   |/    \ \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \     
{Fore.YELLOW}|   |   |  \/        \  \___|  | \// __ \|  |_> >  ___/     
{Fore.YELLOW}|___|___|  /_______  /\___  >__|  (____  /   __/ \___  >    
         \/        \/     \/           \/|__|        \/     
{Fore.WHITE}{Style.BRIGHT}[+]=========================================================[+]
{Fore.CYAN}    Developed & Refactored by: SPY-E | Indonesia OSINT
{Fore.CYAN}    Engine Core              : Instaloader Framework Pro
{Fore.WHITE}[+]=========================================================[+]
"""
    print(logo)

def print_status(message, type_status="info"):
    """Fungsi helper untuk mencetak pesan log berformat warna."""
    if type_status == "success":
        print(f"{Fore.GREEN}[+] {message}")
    elif type_status == "error":
        print(f"{Fore.RED}[-] Error: {message}")
    elif type_status == "warning":
        print(f"{Fore.YELLOW}[!] Peringatan: {message}")
    else:
        print(f"{Fore.BLUE}[*] {message}")
