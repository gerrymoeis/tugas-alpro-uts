"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

number = int(input("Masukkan Angka Faktorial: ").strip())
numbers = (range(number, 0, -1))

def multiply(numbers):
    total = 1
    for n in numbers:
        total *= n
    
    return total

print(f"Nilai Faktorial dari {number}:")
print("x".join(str(n) for n in numbers))
print(multiply(numbers))