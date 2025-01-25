#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Brute Force Shell Finder

import requests
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# File konfigurasi
TARGET_FILE = "target.txt"  # File berisi target URL
WORDLIST_FILE = "wordlist.txt"  # File berisi daftar endpoint shell
OUTPUT_FILE = "result_shell.txt"  # File untuk menyimpan hasil
REQUEST_TIMEOUT = 5  # Timeout request dalam detik

def check_url(url):
    """Memeriksa apakah URL memberikan status kode 200."""
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        pass
    return False

def brute_force(targets, endpoints):
    """Melakukan brute force pada target URL menggunakan endpoint."""
    results = []
    for target in targets:
        print("\nScanning target: {}".format(target))
        found = False
        for endpoint in endpoints:
            url = target.rstrip("/") + "/" + endpoint
            if check_url(url):
                print("{}[FOUND] {} (200 OK){}".format(Fore.GREEN, url, Style.RESET_ALL))
                results.append("[FOUND] {} (200 OK)".format(url))
                found = True
            else:
                print("{}[NOT FOUND] {}{}".format(Fore.RED, url, Style.RESET_ALL))
        if not found:
            print("{}[NO SHELL FOUND]{}".format(Fore.YELLOW, Style.RESET_ALL))
            results.append("[NO SHELL FOUND] {}".format(target))
    return results

def main():
    try:
        # Membaca daftar target
        with open(TARGET_FILE, "r") as f:
            targets = f.read().splitlines()

        # Membaca daftar endpoint
        with open(WORDLIST_FILE, "r") as f:
            endpoints = f.read().splitlines()

        # Mulai brute force
        results = brute_force(targets, endpoints)

        # Simpan hasil
        with open(OUTPUT_FILE, "w") as f:
            f.write("\n".join(results))
        print("\n{}Proses selesai. Hasil disimpan di {}{}".format(Fore.GREEN, OUTPUT_FILE, Style.RESET_ALL))

    except IOError as e:
        print("{}Error: {}{}".format(Fore.RED, e, Style.RESET_ALL))

if __name__ == "__main__":
    main()
