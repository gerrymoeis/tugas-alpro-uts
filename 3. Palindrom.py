"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

sentence = input("Masukkan kalimat bebas:\n").strip()
is_palindrom = False

palindrom = "".join([letter for letter in sentence.lower() if letter.isalpha()])

if palindrom == palindrom[::-1]: is_palindrom = True

print(f"Kalimat '{sentence}' {'adalah' if is_palindrom else 'bukanlah'} Palindrom")
print(f"Karena '{sentence}' {'sama' if is_palindrom else 'berbeda'} dengan '{sentence[::-1]}'")