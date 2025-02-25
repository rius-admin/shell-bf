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
MAX_THREADS = 99    # Jumlah thread maksimal untuk paralelisasi (meningkatkan kecepatan)
session = requests.Session()
session.headers.update({"User-Agent": "BruteShellFinder/1.0"})

def banner():
    print(Fore.CYAN + "        //  ")
    print("        \\\      /=============================\\ ")
    print("         ||    # |  --------------------      # \\ ")
    print("         ||##### |  Cyber Sederhana Team      ## ] ")
    print("         ||    # |  --------------------      # / ")
    print("          \\\    \=============================/  ")
    print("          // ")
    print(Fore.YELLOW + "       contoh : ( https://cybersederhanateam.id )" + Style.RESET_ALL)

def check_url(url):
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT, allow_redirects=False)
        if response.status_code == 200:
            return url
    except requests.exceptions.RequestException:
        pass
    return None

def load_wordlist(wordlist_file):
    try:
        with open(wordlist_file, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(Fore.RED + "Error: File " + wordlist_file + " tidak ditemukan!" + Style.RESET_ALL)
        return []

def brute_force_worker(target, paths):
    found = []
    for path in paths:
        url = f"{target.rstrip('/')}/{path}"
        result = check_url(url)
        if result:
            found.append(result)
            print(Fore.GREEN + "[FOUND] " + result + Style.RESET_ALL)
    return found

def brute_force(target, paths):
    print(Fore.BLUE + "\n[INFO] Attack target: " + target + Style.RESET_ALL)
    results = []

    if not paths:
        print(Fore.RED + "[ERROR] Wordlist kosong!" + Style.RESET_ALL)
        return

    chunk_size = max(len(paths) // MAX_THREADS, 1)
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(brute_force_worker, target, paths[i:i + chunk_size])
                   for i in range(0, len(paths), chunk_size)]

        for future in concurrent.futures.as_completed(futures):
            results.extend(future.result())

    if results:
        print(Fore.GREEN + "\n[INFO] " + str(len(results)) + " shell ditemukan:" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "\n[NO SHELL FOUND] Yha kosong :(" + Style.RESET_ALL)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    banner()

    wordlist_file = 'wordlist.txt'
    wordlist = load_wordlist(wordlist_file)
    if not wordlist:
        return

    while True:
        target = input(Fore.GREEN + "       Scan-bf  ==> " + Style.RESET_ALL).strip()

        if not target.startswith(("http://", "https://")):
            print(Fore.RED + "Error: URL harus diawali dengan 'http://' atau 'https://'" + Style.RESET_ALL)
            continue

        brute_force(target, wordlist)

        continue_prompt = input(Fore.YELLOW + "Ingin melakukan brute force lagi? (y/n): " + Style.RESET_ALL).strip().lower()
        if continue_prompt != 'y':
            print(Fore.GREEN + "Thx udah mampir!" + Style.RESET_ALL)
            break

        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
