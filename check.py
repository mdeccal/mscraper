import requests
import os
from concurrent.futures import ThreadPoolExecutor
import time
from colorama import Fore, init

# Renklerin düzgün görünmesi için terminali başlatıyoruz
init(autoreset=True)

def test_proxy(proxy):
    """Proxy'nin çalışıp çalışmadığını test eder ve anında sonucu ekrana yazar."""
    try:
        # HTTP istek gönder
        response = requests.get('http://www.google.com', proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(Fore.GREEN + f"{proxy} -> ÇALIŞIYOR", flush=True)
            return proxy, "ÇALIŞIYOR"
        print(Fore.RED + f"{proxy} -> BOZUK", flush=True)
        return proxy, "BOZUK"
    except requests.RequestException:
        print(Fore.RED + f"{proxy} -> BOZUK", flush=True)
        return proxy, "BOZUK"

def save_working_proxies():
    """Çalışan proxy'leri türüne göre dosyalara kaydeder."""
    folder = "cikti"
    working_proxies = {"http": [], "socks5": [], "socks4": []}

    # Çıktı klasöründeki proxy dosyalarını oku
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder, filename)
            with open(file_path, "r") as file:
                proxies = file.readlines()

            # Proxy'leri denetle
            for proxy in proxies:
                proxy = proxy.strip()
                if test_proxy(proxy)[1] == "ÇALIŞIYOR":
                    # Proxy çalışıyorsa, türüne göre kaydet
                    if "http" in filename:
                        working_proxies["http"].append(proxy)
                    elif "socks5" in filename:
                        working_proxies["socks5"].append(proxy)
                    elif "socks4" in filename:
                        working_proxies["socks4"].append(proxy)

    # Çalışan proxy'leri dosyalara yaz
    for typ in working_proxies:
        file_path = os.path.join(folder, f"{typ}.txt")
        with open(file_path, "w") as file:
            for proxy in working_proxies[typ]:
                file.write(proxy + "\n")
        print(Fore.GREEN + f"{typ} proxy'leri {file_path} dosyasına kaydedildi.")

def check_proxies():
    """Proxy'leri denetler ve çalışıp çalışmadığını kontrol eder."""
    print(Fore.YELLOW + "Proxy'ler denetleniyor...")

    # Çıktı klasöründeki tüm proxy dosyalarını denetle
    folder = "cikti"
    all_proxies = []

    if os.path.exists(folder):
        for filename in os.listdir(folder):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder, filename)
                with open(file_path, "r") as file:
                    proxies = file.readlines()
                    all_proxies.extend([proxy.strip() for proxy in proxies])

        # Paralel olarak proxyleri denetlemek için ThreadPoolExecutor kullan
        with ThreadPoolExecutor(max_workers=20) as executor:  # max_workers = aynı anda test edilecek proxy sayısı
            results = executor.map(test_proxy, all_proxies)

        # Çalışan proxy'leri kaydetmek ister misiniz?
        save_choice = input(Fore.YELLOW + "\nÇalışan proxy'leri kaydetmek ister misiniz? (E/H): ").strip().lower()
        if save_choice == "e":
            save_working_proxies()
    else:
        print(Fore.RED + f"{folder} klasörü bulunamadı.")

    input(Fore.YELLOW + "\nAna menüye dönmek için bir tuşa basın...")

if __name__ == "__main__":
    check_proxies()


# HANGİ OROSPU EVLADI ÇALARSA ONUN AMINA KOYMAYA HAZIRIM XD