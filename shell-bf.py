#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Script by DarkVairous
# Edited by Mr.Rius

import requests
import os
from urllib2 import Request, urlopen, URLError, HTTPError

WORDLIST_FILE = 'wordlist.txt'
MAX_THREADS = 80 

def clear_screen():
    # Membersihkan layar konsol
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    # Menampilkan banner aplikasi
    clear_screen()
    print("=" * 69)
    print("                _                                        ")
    print("               | | ___   __ _       ___  ___ __ _ _ __   ")
    print("               | |/ _ \\ / _` |-----/ __|/ __/ _` | '_  \\ ")
    print("               | | (_) | (_| |-----\\__ \\ (_| (_| | | | |")
    print("               |_|\\___/ \\__, |-----|___/\\___\\__,_|_| |_|")
    print("                           | | ")
    print("                        __/_/  ")
    print("=" * 69)

def check_admin_panel(url, session):
    # Memeriksa apakah URL mengarah ke halaman admin
    try:
        response = session.get(url, timeout=5)
        if response.status_code == 200:
            print("[Ditemukan] => {}".format(url))
    except requests.RequestException:
        pass

def find_admin():
    # Fungsi utama untuk menemukan halaman admin
    if not os.path.isfile(WORDLIST_FILE):
        print("Error: File '{}' tidak ditemukan.".format(WORDLIST_FILE))
        return
     print(" ") 
     print(" ") 
    target = input("Masukkan target (contoh: target.com): ").strip()

    with open(WORDLIST_FILE, "r") as file:
        paths = [line.strip() for line in file if line.strip()]

    if not paths:
        print("Wordlist kosong atau tidak valid.")
        return

    print("\nMemulai pemindaian...\n")

    session = requests.Session()
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for path in paths:
            url = "http://{}/{}".format(target, path)
            executor.submit(check_admin_panel, url, session)

if __name__ == "__main__":
    banner()
    find_admin()
