#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Editor recode Mr.Rius

import requests
from colorama import Fore, Style, init

# Inisialisasi Colorama
init(autoreset=True)

# File yang berisi target URL (satu per baris)
target_file = 'target.txt'

# File yang berisi daftar endpoint shell yang umum
wordlist_file = 'wordlist.txt'

# Nama file untuk menyimpan hasil scanning
result_file = 'result_shell.txt'

# Timeout untuk request
REQUEST_TIMEOUT = 5

# Fungsi untuk mengecek apakah URL dapat diakses dan status code 200
def check_url(url):
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException as e:
        print("Error saat mengakses {}: {}".format(url, e))
    return False

# Baca file target.txt untuk mendapatkan daftar target URL
try:
    with open(target_file, 'r') as f:
        targets = f.read().splitlines()
except IOError:
    print("File {} tidak ditemukan.".format(target_file))
    exit()

# Baca file wordlist.txt untuk mendapatkan daftar endpoint shell
try:
    with open(wordlist_file, 'r') as f:
        wordlist = f.read().splitlines()
except IOError:
    print("File {} tidak ditemukan.".format(wordlist_file))
    exit()

# Buka file untuk menuliskan hasil
with open(result_file, 'w') as result:
    # Mulai proses scanning setiap target
    for target in targets:
        print("\nScanning target: {}".format(target))
        result.write("\nScanning target: {}\n".format(target))
        
        found_any = False
        
        # Loop setiap endpoint di wordlist
        for path in wordlist:
            url = target.rstrip('/') + '/' + path
            
            # Cek apakah URL valid dan dapat diakses (status code 200)
            if check_url(url):
                print("{}[Ditemukan] {} (200 OK){}".format(Fore.GREEN, url, Style.RESET_ALL))
                result.write("[Ditemukan] {} (200 OK)\n".format(url))
                found_any = True
            else:
                print("{}[Tidak ditemukan] {}{}".format(Fore.RED, url, Style.RESET_ALL))
        
        if not found_any:
            print("{}[Tidak ada shell yang ditemukan untuk target ini]{}".format(Fore.YELLOW, Style.RESET_ALL))
            result.write("[Tidak ada shell yang ditemukan untuk target ini]\n")

print("\nProses selesai. Hasil disimpan di {}".format(result_file))
