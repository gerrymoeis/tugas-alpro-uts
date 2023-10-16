"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

[num1, num2, num3] = [num for num in input("Masukan 3 angka Dalam Format (1, 2, 3): ").strip().split(", ")]

def cek_digit_belakang(num1, num2, num3):
    digits = sorted([num1[-1], num2[-1], num3[-1]])
    count = 0
    for digit in digits:
        if digits[1] == digit: count += 1

    return True if count > 1 else False

print(cek_digit_belakang(num1, num2, num3))