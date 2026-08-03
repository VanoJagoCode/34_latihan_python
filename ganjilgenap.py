def cek_ganjil_genap(angka: int) -> str:
  if angka % 2 == 0:
    return "Genap"
  else:
    return "Ganjil"


def main() -> None:
  bilangan = 7
  hasil = cek_ganjil_genap(bilangan)
  print(f"Angka {bilangan} adalah bilangan {hasil}")
  

if __name__ == "__main__":
  main()
  
