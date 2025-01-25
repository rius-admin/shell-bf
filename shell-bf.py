#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Brute Shell Finder by Cyber Sederhana Team

import requests
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

REQUEST_TIMEOUT = 5  # Timeout permintaan dalam detik


def banner():
    """Menampilkan banner tim dengan tampilan sesuai permintaan."""
    print(f"{Fore.BLUE}" + "=" * 50)
    print(f"{Fore.GREEN}" + "         Cyber Sederhana Team         ")
    print(f"{Fore.BLUE}" + "=" * 50 + f"{Style.RESET_ALL}\n")
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


def load_wordlist(wordlist_file):
    """Memuat daftar endpoint shell dari file wordlist.txt."""
    try:
        with open(wordlist_file, 'r') as file:
            wordlist = file.read().splitlines()
        return wordlist
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File {wordlist_file} tidak ditemukan!{Style.RESET_ALL}")
        return []


def brute_force(target, paths):
    """Melakukan brute force untuk menemukan shell di target."""
    print(f"\n{Fore.BLUE}[INFO] Memulai brute force pada target: {target}{Style.RESET_ALL}")
    found = False

    for path in paths:
        url = f"{target.rstrip('/')}/{path}"
        if check_url(url):
            print(f"{Fore.GREEN}[FOUND] {url} (200 OK){Style.RESET_ALL}")
            found = True
        else:
            print(f"{Fore.RED}[NOT FOUND] {url}{Style.RESET_ALL}")
    
    if not found:
        print(f"{Fore.YELLOW}[NO SHELL FOUND] Tidak ada shell ditemukan pada target ini.{Style.RESET_ALL}")


def main():
    banner()

    # Memuat file wordlist.txt
    wordlist_file = 'wordlist.txt'
    wordlist = load_wordlist(wordlist_file)
    if not wordlist:
        return  # Jika tidak ada wordlist yang valid, keluar dari program

    target = input(f"{Fore.GREEN}Masukkan URL target (contoh: http://example.com): {Style.RESET_ALL}").strip()

    # Validasi input URL
    if not target.startswith("http://") and not target.startswith("https://"):
        print(f"{Fore.RED}Error: URL harus diawali dengan 'http://' atau 'https://'{Style.RESET_ALL}")
        return

    # Memulai brute force
    brute_force(target, wordlist)


if __name__ == "__main__":
    main()
