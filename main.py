import sys
import time
import subprocess

def efek_mengetik(teks, jeda=0.03):
    """Fungsi untuk memunculkan teks per huruf seperti diketik."""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(jeda)
    print() # Pindah ke baris baru setelah kalimat selesai

def jalankan_menu_utama():
    # Teks perkenalan sesuai permintaan
    perkenalan = (
        "Halo perkenalkan semuanya namaku Vano Dwiki Ardelon 11-TKJ-2/34.\n"
        "Selamat datang di tempatku latihan Code Python.\n"
        "Disini kalian bisa memilih beberapa Code yang telah aku buat. Silahkan pilih mana yang anda butuhkan.\n"
    )
    
    # Memanggil animasi mengetik
    efek_mengetik(perkenalan, jeda=0.02) # Angka 0.02 mengatur kecepatan ketikan
    
    while True:
        print("\n=== MENU UTAMA ===")
        print("A. Modul Matematika")
        print("B. Perhitungan persegi panjang")
        print("X. Keluar")
        print("==================")
        
        pilihan = input("Masukkan pilihan (A/B/X): ").strip().upper()
        
        if pilihan == 'A':
            print("\n[Membuka ModulMatematika.py...]")
            try:
                # sys.executable memastikan Python yang digunakan sama dengan yang menjalankan file utama ini
                subprocess.run([sys.executable, "ModulMatematika.py"])
            except FileNotFoundError:
                print("Error: File 'ModulMatematika.py' tidak ditemukan di dalam folder ini.")
                
        elif pilihan == 'B':
            print("\n[Membuka PersegiPanjang.py...]")
            try:
                subprocess.run([sys.executable, "PersegiPanjang.py"])
            except FileNotFoundError:
                print("Error: File 'PersegiPanjang.py' tidak ditemukan di dalam folder ini.")
                
        elif pilihan == 'X':
            print("\nKeluar dari program. Terima kasih!")
            break
            
        else:
            print("\nPilihan tidak valid. Harap ketik A, B, atau X.")

if __name__ == "__main__":
    jalankan_menu_utama()
  
