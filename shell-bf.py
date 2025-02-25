#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Script by DarkVairous
# Edited by Mr.Rius

import requests
import os
from concurrent.futures import ThreadPoolExecutor

def banner():
    print("=" * 69)
    print("                _                                        ")
    print("               | | ___   __ _       ___  ___ __ _ _ __   ")
    print("               | |/ _ \\ / _` |-----/ __|/ __/ _` | '_ \\ ")
    print("               | | (_) | (_| |-----\\__ \\ (_| (_| | | | |")
    print("               |_|\\___/ \\__, |-----|___/\\___\\__,_|_| |_|")
    print("                           | | ")
    print("                        __/_/  ")
    print("=" * 69)

def check_admin_panel(url, session):
    try:
        response = session.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[Ditemukan] => {url}")
    except requests.RequestException:
        pass

def find_admin():
    wordlist_file = "wordlist.txt"
    target = input("Masukkan target (contoh: target.com): ").strip()

    if not os.path.isfile(wordlist_file):
        print(f"File '{wordlist_file}' tidak ditemukan.")
        return

    with open(wordlist_file, "r") as file:
        paths = [line.strip() for line in file if line.strip()]

    if not paths:
        print("Wordlist kosong atau tidak valid.")
        return

    print("\nMemulai pemindaian...\n")

    session = requests.Session()
    with ThreadPoolExecutor(max_workers=50) as executor:
        for path in paths:
            url = f"http://{target}/{path}"
            executor.submit(check_admin_panel, url, session)

if __name__ == "__main__":
    banner()
    find_admin()
