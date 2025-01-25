#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Script Brute Shell by Mr.Rius

import requests
from colorama import Fore, Style, init

# Inisialisasi Colorama
init(autoreset=True)

# File yang berisi target URL
target_file = 'target.txt'

# File yang berisi daftar endpoint shell
wordlist_file = 'wordlist.txt'

# Nama file untuk menyimpan hasil
result_file = 'result_shell.txt'

# Timeout request
REQUEST_TIMEOUT = 5

# Fungsi untuk mengecek endpoint shell
def check_shell(target, endpoint):
    url = target.rstrip('/') + '/' + endpoint
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            return True, url
    except requests.exceptions.RequestException:
        return False, None
    return False, None

# Load daftar target dari file
try:
    with open(target_file, 'r') as f:
        targets = f.read().splitlines()
except IOError:
    print(f"{Fore.RED}File target.txt tidak ditemukan.{Style.RESET_ALL}")
    exit()

# Load daftar endpoint dari file
try:
    with open(wordlist_file, 'r') as f:
        endpoints = f.read().splitlines()
except IOError:
    print(f"{Fore.RED}File wordlist.txt tidak ditemukan.{Style.RESET_ALL}")
    exit()

# Hasil scanning akan disimpan di result_shell.txt
with open(result_file, 'w') as result:
    for target in targets:
        print(f"\n{Fore.CYAN}Scanning target: {target}{Style.RESET_ALL}")
        result.write(f"Scanning target: {target}\n")
        found = False

        for endpoint in endpoints:
            success, shell_url = check_shell(target, endpoint)
            if success:
                print(f"{Fore.GREEN}[Ditemukan] Shell: {shell_url} (200 OK){Style.RESET_ALL}")
                result.write(f"[Ditemukan] Shell: {shell_url} (200 OK)\n")
                found = True
                break
            else:
                print(f"{Fore.YELLOW}[Tidak ditemukan] {target}/{endpoint}{Style.RESET_ALL}")

        if not found:
            print(f"{Fore.RED}[Tidak ada shell ditemukan untuk target ini]{Style.RESET_ALL}")
            result.write("[Tidak ada shell ditemukan untuk target ini]\n")

print(f"\n{Fore.CYAN}Proses selesai. Hasil disimpan di {result_file}{Style.RESET_ALL}")
