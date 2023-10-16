"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

numbers = [*range(int(input("Masukkan Jumlah Bilangan Fibonacci: ").strip()))]

base = {0: 0, 1: 1}
def fibonacci_of(n):
    if n in base:
        return base[n]
    base[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
    return base[n]

def fibonacci(numbers):
    return [str(fibonacci_of(n)) for n in numbers]

print(f"Daftar {len(numbers)} Bilangan Fibonacci yaitu:")
print(", ".join(fibonacci(numbers)))

# Versi Manual (Lebih Lambat)
# def fibonacci_of(n):
#     if n in {0, 1}:
#         return n
#     return fibonacci_of(n - 1) + fibonacci_of(n - 2)

# def fibonacci(numbers):
#     return [str(fibonacci_of(n)) for n in numbers]