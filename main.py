#!/usr/bin/env python3
"""
Project Name: InScrape Pro - Instagram OSINT Tool
Author      : SPY-E | Indonesia OSINT
Description : Refactored professional Instagram profile scraper with anti-block mechanisms.
"""

import sys
from colorama import Fore, Style
from src.banner import show_banner, print_status
from src.utils import validate_input
from src.core import InstagramOSINT

def main():
    # 1. Tampilkan Visual Banner identitas brand kamu
    show_banner()
    
    # 2. Inisialisasi Engine Core Instaloader
    bot = InstagramOSINT()
    
    # 3. Alur Otentikasi Pengguna
    print(f"{Fore.WHITE}{Style.BRIGHT}[ Tahap 1: Otentikasi Akses API ]")
    my_username = validate_input(f"{Fore.CYAN}Masukkan Username Akun Anda: {Fore.WHITE}")
    my_password = validate_input(f"{Fore.CYAN}Masukkan Password Akun Anda: {Fore.WHITE}")
    print(Style.RESET_ALL)
    
    if not bot.attempt_login(my_username, my_password):
        print_status("Proses dihentikan karena kegagalan login.", "error")
        sys.exit(1)
        
    print("\n" + "="*60 + "\n")
    
    # 4. Input Target Akun Intelijen
    print(f"{Fore.WHITE}{Style.BRIGHT}[ Tahap 2: Penentuan Target OSINT ]")
    target = validate_input(f"{Fore.YELLOW}Masukkan Username Target (Tanpa @): {Fore.WHITE}")
    print(Style.RESET_ALL)
    
    # 5. Penarikan Data Profil & Cetak Hasil
    profile_obj, data_dict = bot.fetch_profile_data(target)
    
    if data_dict:
        print(f"\n{Fore.GREEN}{Style.BRIGHT}[ HASIL ANALISIS METADATA PROFIL ]")
        print(f"{Fore.GREEN}="*40)
        for key, value in data_dict.items():
            print(f"{Fore.WHITE}{key:<25} : {Fore.CYAN}{value}")
        print(f"{Fore.GREEN}="*40)
        
        # 6. Penarikan Relasi Data Pengikut (Aman & Dibatasi agar tidak terkena limit)
        # Parameter 'limit=30' untuk keamanan akun dari blokir algoritma Meta
        bot.dump_relations(profile_obj, limit=30)
    else:
        print_status("Gagal memproses data intelijen untuk target ini.", "error")
        
    print(f"\n{Fore.GREEN}[+] Selesai. Terima kasih telah menggunakan tool dari Indonesia OSINT.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Proses dibatalkan secara paksa oleh pengguna (Ctrl+C). Keluar...")
        sys.exit(0)
