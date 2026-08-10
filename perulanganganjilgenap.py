def cek_ganjil_genap(angka: int) -> str:
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"


def main() -> None:
    print("=== Program Pengecekan Ganjil/Genap ===")
    print("Ketik huruf 'x' lalu tekan Enter untuk menutup/menghentikan program.\n")
    
    while True:
        # Meminta input dari pengguna secara dinamis
        input_user = input("Masukkan sebuah angka: ")
        
        # Mengecek apakah input adalah karakter untuk keluar ('x')
        if input_user.lower() == 'x':
            print("Program dihentikan. Terima kasih!")
            break  # Memutus perulangan
        
        # Memastikan input yang dimasukkan benar-benar angka
        try:
            bilangan = int(input_user)
            hasil = cek_ganjil_genap(bilangan)
            print(f"-> Angka {bilangan} adalah bilangan {hasil}\n")
        except ValueError:
            print("-> Input tidak valid! Harap masukkan angka bulat.\n")


if __name__ == "__main__":
    main()