#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Brute Shell Finder by Cyber Sederhana Team

import requests
from colorama import Fore, Style, init
import os
import threading

# Inisialisasi colorama
init(autoreset=True)

REQUEST_TIMEOUT = 3  # Timeout permintaan lebih singkat (dalam detik)
MAX_THREADS = 10     # Jumlah thread maksimal untuk paralelisasi

# Inisialisasi session untuk connection pooling
session = requests.Session()
session.headers.update({"User-Agent": "BruteShellFinder/1.0"})

def banner():
    """Menampilkan banner tim dengan tampilan sesuai permintaan."""
    print(f"{Fore.BLUE}" + "=" * 75)
    print(" ") 
    print(f"{Fore.GREEN}" + "                     Cyber Sederhana Team         ")
    print(" ") 
    print(f"{Fore.BLUE}" + "=" * 75 + f"{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}by Mr.Rius{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}gunain untuk tickung shell anak cibel ya hehe{Style.RESET_ALL}\n")


def check_url(url):
    """Memeriksa apakah URL memberikan status 200 menggunakan session."""
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            return url  # Mengembalikan URL yang berhasil ditemukan
    except requests.exceptions.RequestException:
        pass
    return None


def load_wordlist(wordlist_file):
    """Memuat daftar endpoint shell dari file wordlist.txt."""
    try:
        with open(wordlist_file, 'r') as file:
            wordlist = file.read().splitlines()
        return wordlist
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File {wordlist_file} tidak ditemukan!{Style.RESET_ALL}")
        return []


def brute_force_worker(target, paths, results):
    """Thread worker untuk melakukan brute force pada target."""
    for path in paths:
        url = f"{target.rstrip('/')}/{path}"
        result = check_url(url)
        if result:
            results.append(result)
            print(f"{Fore.GREEN}[FOUND] {url} (200 OK){Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[NOT FOUND] {url}{Style.RESET_ALL}")


def brute_force(target, paths):
    """Melakukan brute force untuk menemukan shell di target dengan paralelisasi menggunakan thread."""
    print(f"\n{Fore.BLUE}[INFO] Memulai brute force pada target: {target}{Style.RESET_ALL}")

    results = []
    threads = []

    # Membagi wordlist menjadi beberapa bagian untuk di proses paralel
    chunk_size = len(paths) // MAX_THREADS
    for i in range(0, len(paths), chunk_size):
        chunk = paths[i:i+chunk_size]
        thread = threading.Thread(target=brute_force_worker, args=(target, chunk, results))
        threads.append(thread)
        thread.start()

    # Menunggu semua thread selesai
    for thread in threads:
        thread.join()

    if results:
        print(f"{Fore.GREEN}[INFO] Done ditemukan √ {len(results)} shell.{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}[NO SHELL FOUND] Yha kosong :({Style.RESET_ALL}")


def main():
    while True:
        # Menampilkan banner dan meminta URL target
        banner()

        # Memuat file wordlist.txt
        wordlist_file = 'wordlist.txt'
        wordlist = load_wordlist(wordlist_file)
        if not wordlist:
            return  # Jika tidak ada wordlist yang valid, keluar dari program

        target = input(f"{Fore.GREEN}( contoh: https://cybersederhanateam.id ): {Style.RESET_ALL}").strip()

        # Validasi input URL
        if not target.startswith("http://") and not target.startswith("https://"):
            print(f"{Fore.RED}Error: diawali dengan 'http://' atau 'https://'{Style.RESET_ALL}")
            continue

        # Memulai brute force
        brute_force(target, wordlist)

        # Menanyakan apakah ingin melanjutkan ke target lain
        continue_prompt = input(f"{Fore.YELLOW}Ingin melakukan brute force lagi? (y/n): {Style.RESET_ALL}").strip().lower()
        if continue_prompt != 'y':
            print(f"{Fore.GREEN}Terima kasih telah menggunakan tool ini!{Style.RESET_ALL}")
            break

        # Kembali ke "tempat kosong" (clear screen)
        os.system('clear')  # untuk Linux/macOS
        # os.system('cls')  # untuk Windows, gunakan ini jika di cmd atau PowerShell


if __name__ == "__main__":
    main()
