#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Script by Mr.Rius

import requests
import os
from urllib.parse import urljoin

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def scan_path(session, base_url, path):
    """Memindai satu path dengan menggunakan session untuk mempercepat koneksi."""
    full_url = urljoin(base_url, path)
    try:
        response = session.get(full_url, timeout=5)
        if response.status_code == 200:
            print(f"[+] Path ditemukan: {full_url} (Status Code: {response.status_code})")
    except requests.exceptions.RequestException:
        pass

def scan_paths(base_url, wordlist_file="wordlist.txt"):
    """Memindai daftar path dengan menggunakan session reuse untuk mempercepat scanning."""
    if not os.path.exists(wordlist_file):
        print(f"[!] File {wordlist_file} tidak ditemukan.")
        return

    with open(wordlist_file, "r") as file:
        paths = [line.strip() for line in file if line.strip()]

    print(f"     Progress scan '{wordlist_file}' ke {base_url}...\n")

    # Menggunakan session untuk mempercepat koneksi HTTP
    with requests.Session() as session:
        for path in paths:
            scan_path(session, base_url, path)

# Program utama
clear_screen()

print(" ") 
print("     \nTarget: target-shell.net\n") 
target_url = input("     Scan > ").strip()
print(" ") 

# Menambahkan skema (http://) jika belum ada
if not target_url.startswith(("http://", "https://")):
    target_url = "http://" + target_url

# Menambahkan tanda "/" di akhir URL jika belum ada
if not target_url.endswith('/'):
    target_url += '/'

scan_paths(target_url)
