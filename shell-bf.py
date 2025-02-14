#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Brute Shell Finder by Cyber Sederhana Team

import requests
from colorama import Fore, Style, init
import os
import concurrent.futures

# Inisialisasi colorama
init(autoreset=True)

REQUEST_TIMEOUT = 3  # Timeout permintaan (dalam detik)
MAX_THREADS = 50     # Jumlah thread maksimal untuk paralelisasi
session = requests.Session()
session.headers.update({"User-Agent": "BruteShellFinder/1.0"})

def banner():
    """Menampilkan banner tim."""
    print(f"""
        //  
        \\\      /=============================\ 
         ||    # |  --------------------      #\\ 
         ||##### |  Cyber Sederhana Team      ##] 
         ||    # |  --------------------      #/ 
          \\\    \=============================/  
          // 
          
       {Fore.YELLOW}contoh : ( https://cybersederhanateam.id ){Style.RESET_ALL}
    """)

def check_url(url):
    """Memeriksa apakah URL memberikan status 200."""
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            return url
    except requests.exceptions.RequestException:
        pass
    return None

def load_wordlist(wordlist_file):
    """Memuat daftar endpoint shell dari file wordlist."""
    try:
        with open(wordlist_file, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File {wordlist_file} tidak ditemukan!{Style.RESET_ALL}")
        return []

def brute_force_worker(target, paths):
    """Melakukan brute force pada target dengan mengecek URL."""
    found = []
    for path in paths:
        url = f"{target.rstrip('/')}/{path}"
        result = check_url(url)
        if result:
            found.append(result)
    return found

def brute_force(target, paths):
    """Melakukan brute force untuk menemukan shell di target."""
    print(f"\n{Fore.BLUE}[INFO] Attack target: {target}{Style.RESET_ALL}")
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        chunk_size = len(paths) // MAX_THREADS + 1
        for i in range(0, len(paths), chunk_size):
            chunk = paths[i:i + chunk_size]
            futures.append(executor.submit(brute_force_worker, target, chunk))

        for future in concurrent.futures.as_completed(futures):
            results.extend(future.result())

    if results:
        print(f"\n{Fore.GREEN}[INFO] {len(results)} shell ditemukan:{Style.RESET_ALL}")
        for url in results:
            print(f"{Fore.GREEN}{url}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.YELLOW}[NO SHELL FOUND] Yha kosong :({Style.RESET_ALL}")

def main():
    os.system('clear')  # Bersihkan layar (Linux/macOS)
    # os.system('cls')  # Bersihkan layar (Windows)
    banner()

    wordlist_file = 'wordlist.txt'
    wordlist = load_wordlist(wordlist_file)
    if not wordlist:
        return

    while True:
        target = input(f"{Fore.GREEN}       Scan-bf  ==> {Style.RESET_ALL}").strip()

        if not target.startswith(("http://", "https://")):
            print(f"{Fore.RED}Error: URL harus diawali dengan 'http://' atau 'https://'{Style.RESET_ALL}")
            continue

        brute_force(target, wordlist)

        continue_prompt = input(f"{Fore.YELLOW}Ingin melakukan brute force lagi? (y/n): {Style.RESET_ALL}").strip().lower()
        if continue_prompt != 'y':
            print(f"{Fore.GREEN}Thx udah mampir!{Style.RESET_ALL}")
            break
        os.system('clear')  # Bersihkan layar

if __name__ == "__main__":
    main()
