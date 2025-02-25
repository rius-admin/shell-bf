import requests
import os
from concurrent.futures import ThreadPoolExecutor

# Konfigurasi
TARGET_URL = 'http://contoh.com'  # Ganti dengan URL target
WORDLIST_FILE = 'wordlist.txt'    # Pastikan file wordlist.txt berada di direktori yang sama
MAX_THREADS = 50                  # Jumlah maksimum thread untuk paralelisme

# Fungsi untuk memeriksa keberadaan halaman admin
def check_admin_path(path):
    url = f"{TARGET_URL.rstrip('/')}/{path.lstrip('/')}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[Ditemukan] {url}")
            return url
    except requests.RequestException:
        pass
    return None

# Memuat wordlist
if not os.path.isfile(WORDLIST_FILE):
    print(f"File '{WORDLIST_FILE}' tidak ditemukan.")
    exit()

with open(WORDLIST_FILE, 'r') as file:
    paths = [line.strip() for line in file if line.strip()]

# Menggunakan ThreadPoolExecutor untuk mempercepat proses
found_paths = []
with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    results = executor.map(check_admin_path, paths)
    found_paths = [result for result in results if result]

if found_paths:
    print("\nHalaman admin yang ditemukan:")
    for path in found_paths:
        print(path)
else:
    print("\nTidak ditemukan halaman admin.")
