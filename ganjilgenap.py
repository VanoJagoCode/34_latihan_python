def cek_ganjil_genap():
    print("\n--- CEK GANJIL / GENAP ---")
    try:
        angka = int(input("Masukkan sebuah angka: "))
        if angka % 2 == 0:
            print(f"-> {angka} adalah bilangan GENAP.")
        else:
            print(f"-> {angka} adalah bilangan GANJIL.")
    except ValueError:
        print("-> Input tidak valid! Harap masukkan angka (bilangan bulat).")

def cek_prima():
    print("\n--- CEK BILANGAN PRIMA ---")
    try:
        angka = int(input("Masukkan sebuah angka: "))
        # Bilangan prima harus lebih besar dari 1
        if angka > 1:
            is_prima = True
            # Mengecek faktor pembagi dari 2 hingga akar kuadrat angka tersebut
            for i in range(2, int(angka ** 0.5) + 1):
                if angka % i == 0:
                    is_prima = False
                    break
            
            if is_prima:
                print(f"-> {angka} ADALAH bilangan prima.")
            else:
                print(f"-> {angka} BUKAN bilangan prima.")
        else:
            print(f"-> {angka} BUKAN bilangan prima.")
    except ValueError:
        print("-> Input tidak valid! Harap masukkan angka (bilangan bulat).")

def main():
    while True:
        print("\n" + "="*30)
        print("          MENU UTAMA          ")
        print("="*30)
        print("a. Cek Ganjil / Genap")
        print("b. Cek Bilangan Prima / Bukan")
        print("c. Exit")
        print("="*30)
        
        # .lower() digunakan agar input 'A' besar tetap terbaca sebagai 'a' kecil
        pilihan = input("Pilih menu (a/b/c): ").lower() 
        
        if pilihan == 'a':
            cek_ganjil_genap()
        elif pilihan == 'b':
            cek_prima()
        elif pilihan == 'c':
            print("\nTerima kasih! Program dihentikan.\n")
            break # Perintah break digunakan untuk keluar dari loop (menghentikan program)
        else:
            print("\n-> Pilihan tidak valid! Silakan ketik a, b, atau c.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
    
