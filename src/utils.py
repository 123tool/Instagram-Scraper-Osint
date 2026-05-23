import time
import random
from colorama import Fore

def anti_block_delay(minimum=2, maximum=5):
    """
    Membuat jeda acak untuk meniru perilaku manusia (human behavior).
    Sangat krusial saat melakukan looping data massal seperti followers.
    """
    delay = random.uniform(minimum, maximum)
    print(f"{Fore.BLACK}{Style.DIM}[Anti-Block] Menunggu {delay:.2f} detik sebelum request berikutnya...")
    time.sleep(delay)

def validate_input(prompt_text):
    """Memastikan user tidak memasukkan string kosong."""
    while True:
        user_input = input(prompt_text).strip()
        if user_input:
            return user_input
        print(f"{Fore.RED}[-] Input tidak boleh kosong! Silakan coba lagi.")
