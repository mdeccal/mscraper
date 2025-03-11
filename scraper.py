import requests
import os
from colorama import init, Fore, Style


init(autoreset=True)


def fetch_proxies():
    # ProxyScrape API URL
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol={typ}&timeout=10000&country=all&ssl=all&anonymity=all"
    
    # Çıktı klasörünü kontrol et, yoksa oluştur
    if not os.path.exists("cikti"):
        os.makedirs("cikti")

    # HTTP, SOCKS4, SOCKS5 için proxy çekme
    protocols = ["http", "socks5", "socks4"]
    
    for protocol in protocols:
        # API'yi çağır
        response = requests.get(url.format(typ=protocol))
        
        if response.status_code == 200:
            proxies = response.text.splitlines()  # Proxyleri satır satır al
            file_path = f"cikti/{protocol}.txt"
            
            # Proxyleri .txt dosyasına kaydet
            with open(file_path, "w") as file:
                for proxy in proxies:
                    file.write(proxy + "\n")
            print(f"{protocol} proxyleri {file_path} dosyasına kaydedildi.")
        else:
            print(f"{protocol} proxyleri alınamadı.")

if __name__ == "__main__":
    fetch_proxies()
