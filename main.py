import os
import subprocess
from colorama import init, Fore, Style

os.system('title Proxy Scraper By : mdeccal - Educational Purpose')
os.system('mode con: cols=110 lines=24')

init(autoreset=True)

def clear_output_folder():
    # cikti klasöründeki tüm dosyaları sil
    output_folder = 'cikti'
    try:
        files = os.listdir(output_folder)
        for file in files:
            file_path = os.path.join(output_folder, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print(Fore.GREEN + "\nÇıktı klasörü temizlendi.")
    except FileNotFoundError:
        print(Fore.RED + "Çıktı klasörü bulunamadı.")
    except Exception as e:
        print(Fore.YELLOW + f"Hata oluştu: {e}")

def banner():
    # Banner yazısı
    print(Fore.GREEN + Style.BRIGHT + """
     ____    ____   ______     ______  _______          _       _______  _______  ________  _______     
    |_   \  /   _|.' ____ \  .' ___  ||_   __ \        / \     |_   __ \|_   __ \|_   __  ||_   __ \    
      |   \/   |  | (___ \_|/ .'   \_|  | |__) |      / _ \      | |__) | | |__) | | |_ \_|  | |__) |   
      | |\  /| |   _.____`.| |          |  __ /      / ___ \     |  ___/  |  ___/  |  _| _   |  __ /    
     _| |_\/_| |_ | \____) |\ `.___.'\ _| |  \ \_  _/ /   \ \_  _| |_    _| |_    _| |__/ | _| |  \ \_  
    |_____||_____| \______.' `.____ .'|____| |___||____| |____||_____|  |_____|  |________||____| |___| 
                                                                                                    
          
                            github: mdeccal <3
                                                                                           
    """)

def menu():
    while True:
        # Ekranı temizle
        os.system('cls' if os.name == 'nt' else 'clear')
        
        banner()  # Banner

        # Ana menü
        
        print(Fore.MAGENTA + Style.BRIGHT + "\n\n\n")
        print(Fore.CYAN + "                                   —————————— Ana Menü —————————— ")
        print("                ")

        # Seçenekler

        print(Fore.GREEN + "                               <<", Fore.WHITE + "1", Fore.GREEN + ">> " + Fore.WHITE + "Taze Proxy Çek ")
        print(Fore.GREEN + "                               <<", Fore.WHITE + "2", Fore.GREEN + ">> " + Fore.WHITE + "Proxy'leri Denetle ")
        print(Fore.GREEN + "                               <<", Fore.WHITE + "3", Fore.GREEN + ">> " + Fore.WHITE + "Klasörü Temizle ")
        print(Fore.RED + "                               Çıkmak için 'q' tuşuna basın.")
        
        choice = input(Fore.CYAN + "\n\nSeçiminizi girin: ")

        if choice == '1':
            print(Fore.BLUE + "\nTaze proxy çekiliyor...\n")
            subprocess.run(['python', 'scraper.py'])  # scraper.py dosyasını çalıştır
        elif choice == '2':
            print(Fore.BLUE + "\nProxy'ler denetleniyor...\n")
            subprocess.run(['python', 'check.py'])  # check.py dosyasını çalıştır
        elif choice == '3':
            print(Fore.YELLOW + "\nÇıktı klasörü temizleniyor...\n")
            clear_output_folder()  # Çıktı klasörünü temizle
        elif choice.lower() == 'q':
            print(Fore.GREEN + "\nÇıkılıyor...\n")
            break
        else:
            print(Fore.RED + "\nGeçersiz seçenek, tekrar deneyin.")
        
        # Ana menüye dönme
        input(Fore.CYAN + "Ana menüye dönmek için Enter'a basın...")

if __name__ == "__main__":
    menu()


# KODLAR MDECCAL'E AİTTİR HERHNAGİ BİRİSİ ÇALARSA HAKKINDA ÇOK HOŞNUT OLMAYACAĞI ŞEYLER OLABİLİR :D