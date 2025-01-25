#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Brute Shell Finder by Cyber Sederhana Team

import os
import requests
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Konfigurasi file
TARGET_FILE = "target.txt"  # Daftar target URL
WORDLIST_FILE = "wordlist.txt"  # Daftar endpoint shell
OUTPUT_FILE = "result_shell.txt"  # File untuk menyimpan hasil
REQUEST_TIMEOUT = 5  # Timeout permintaan dalam detik


def clear_screen():
    """Membersihkan layar terminal."""
    os.system('clear' if os.name == 'posix' else 'cls')


def banner():
    """Menampilkan banner tim."""
    clear_screen()
    print(f"{Fore.CYAN}" + "=" * 40)
    print("         Cyber Sederhana Team")
    print("=" * 40 + f"{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}Gunakan script ini hanya untuk tujuan legal dan etis.{Style.RESET_ALL}\n")


def check_url(url):
    """Memeriksa apakah URL memberikan status 200."""
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        pass
    return False


def brute_force(targets, paths):
    """Melakukan brute force untuk menemukan shell di target."""
    results = []
    for target in targets:
        print(f"\n{Fore.BLUE}[INFO] Scanning target: {target}{Style.RESET_ALL}")
        found = False
        for path in paths:
            url = f"{target.rstrip('/')}/{path}"
            if check_url(url):
                print(f"{Fore.GREEN}[FOUND] {url} (200 OK){Style.RESET_ALL}")
                results.append(f"[FOUND] {url} (200 OK)")
                found = True
            else:
                print(f"{Fore.RED}[NOT FOUND] {url}{Style.RESET_ALL}")
        if not found:
            print(f"{Fore.YELLOW}[NO SHELL FOUND] for {target}{Style.RESET_ALL}")
            results.append(f"[NO SHELL FOUND] {target}")
    return results


def main():
    banner()
    print(f"{Fore.CYAN}Ketik 'start' untuk memulai proses brute shell.{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Ketik 'exit' untuk keluar dari program.{Style.RESET_ALL}")
    
    while True:
        command = input(f"{Fore.GREEN}Cyber Sederhana Team >> {Style.RESET_ALL}").strip().lower()
        
        if command == "start":
            try:
                # Membaca file target
                with open(TARGET_FILE, "r") as f:
                    targets = f.read().splitlines()

                # Membaca file wordlist
                with open(WORDLIST_FILE, "r") as f:
                    paths = f.read().splitlines()

                # Memulai brute force
                results = brute_force(targets, paths)

                # Menyimpan hasil ke file
                with open(OUTPUT_FILE, "w") as f:
                    f.write("\n".join(results))
                print(f"\n{Fore.GREEN}Proses selesai. Hasil disimpan di {OUTPUT_FILE}{Style.RESET_ALL}")
            except FileNotFoundError as e:
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error tak terduga: {e}{Style.RESET_ALL}")
        
        elif command == "exit":
            print(f"{Fore.YELLOW}Keluar dari program. Terima kasih.{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}Perintah tidak dikenal. Ketik 'start' untuk memulai atau 'exit' untuk keluar.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
