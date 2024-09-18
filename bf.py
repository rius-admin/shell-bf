#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Editor recode Mr.Rius

import requests
from colorama import Fore, Style

# File yang berisi target URL (satu per baris)
target_file = 'target.txt'

# File yang berisi daftar endpoint shell yang umum
wordlist_file = 'wordlist.txt'

# Nama file untuk menyimpan hasil scanning
result_file = 'result_shell.txt'

# Fungsi untuk mengecek apakah URL dapat diakses dan status code 200
def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengakses {url}: {e}")
    return False

# Baca file target.txt untuk mendapatkan daftar target URL
try:
    with open(target_file, 'r') as f:
        targets = f.read().splitlines()
except FileNotFoundError:
    print(f"File {target_file} tidak ditemukan.")
    exit()

# Baca file wordlist.txt untuk mendapatkan daftar endpoint shell
try:
    with open(wordlist_file, 'r') as f:
        wordlist = f.read().splitlines()
except FileNotFoundError:
    print(f"File {wordlist_file} tidak ditemukan.")
    exit()

# Buka file untuk menuliskan hasil
with open(result_file, 'w') as result:
    # Mulai proses scanning setiap target
    for target in targets:
        print(f"\nScanning target: {target}")
        result.write(f"\nScanning target: {target}\n")
        
        found_any = False
        
        # Loop setiap endpoint di wordlist
        for path in wordlist:
            url = target.rstrip('/') + '/' + path
            
            # Cek apakah URL valid dan dapat diakses (status code 200)
            if check_url(url):
                print(f"{Fore.GREEN}[Ditemukan] {url} (200 OK){Style.RESET_ALL}")
                result.write(f"[Ditemukan] {url} (200 OK)\n")
                found_any = True
            else:
                print(f"{Fore.RED}[Tidak ditemukan] {url}{Style.RESET_ALL}")
        
        if not found_any:
            print(f"{Fore.YELLOW}[Tidak ada shell yang ditemukan untuk target ini]{Style.RESET_ALL}")
            result.write(f"[Tidak ada shell yang ditemukan untuk target ini]\n")

print(f"\nProses selesai. Hasil disimpan di {result_file}")
