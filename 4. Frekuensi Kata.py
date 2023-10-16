"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

kalimat = input("Masukkan kalimat yang diinginkan: ").strip().split(" ")
kata_input = input("Masukkan kata yang diinginkan: ").strip()

frekuensi_kata = 0
for kata in kalimat:
    if kata.lower() == kata_input.lower(): frekuensi_kata += 1

print(f"Dalam kalimat '{' '.join(kalimat)}'")
if frekuensi_kata > 0:
    print(f"Kata '{kata_input}' muncul sebanyak {frekuensi_kata} kali")
else:
    print(f"Kata '{kata_input}' tidak pernah muncul")