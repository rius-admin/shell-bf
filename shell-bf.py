#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Custom Admin Finder Brute Force

import requests
from colorama import Fore, Style, init
import time

# Inisialisasi colorama
init(autoreset=True)

# File konfigurasi
TARGET_FILE = "target.txt"  # Daftar target URL (satu per baris)
WORDLIST_FILE = "wordlist.txt"  # Daftar path untuk admin (file wordlist)
OUTPUT_FILE = "result_admin_brute.txt"  # File untuk menyimpan hasil
REQUEST_TIMEOUT = 5  # Timeout request dalam detik

# Fungsi untuk memeriksa apakah URL mengembalikan status 200
def check_url(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response_time = round(time.time() - start_time, 2)  # Waktu respons
        if response.status_code == 200:
            return True, response_time
        return False, response_time
    except requests.exceptions.RequestException:
        return False, 0

# Fungsi utama untuk melakukan brute force dengan target dan paths
def brute_force_admin(targets, paths):
    results = []
    for target in targets:
        print(f"\nScanning target: {target}")
        found = False
        for path in paths:
            url = f"{target.rstrip('/')}/{path}"
            is_found, response_time = check_url(url)
            
            # Jika ditemukan, tampilkan hasil dengan waktu respons
            if is_found:
                print(f"{Fore.GREEN}[FOUND] {url} - Response time: {response_time}s{Style.RESET_ALL}")
                results.append(f"[FOUND] {url} - Response time: {response_time}s")
                found = True
            else:
                # Jika tidak ditemukan, hanya tampilkan "not found"
                print(f"{Fore.RED}[NOT FOUND] {url}{Style.RESET_ALL}")
        
        if not found:
            print(f"{Fore.YELLOW}[NO ADMIN PAGE FOUND] for {target}{Style.RESET_ALL}")
            results.append(f"[NO ADMIN PAGE FOUND] {target}")
    
    return results

def main():
    try:
        # Membaca file target (URL)
        with open(TARGET_FILE, "r") as f:
            targets = f.read().splitlines()

        # Membaca file wordlist (path admin)
        with open(WORDLIST_FILE, "r") as f:
            paths = f.read().splitlines()

        # Menjalankan brute force
        results = brute_force_admin(targets, paths)

        # Menyimpan hasil ke file output
        with open(OUTPUT_FILE, "w") as f:
            f.write("\n".join(results))
        
        print(f"\n{Fore.GREEN}Proses selesai. Hasil disimpan di {OUTPUT_FILE}{Style.RESET_ALL}")
    
    except IOError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
