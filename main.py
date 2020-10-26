# DDP LAB-2

# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini
print("SOAL 1 - Mencetak bilangan ")
print("\n")
for i in range(100, 0, -2):
    print(i, end=",")

print("\n\n")  #  \n = karakter untuk membuat enter / baris baru

# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini

print("SOAL 2 - Mencetak Rata - Rata ")
print("\n")
print("contoh 2.1")
print("\n")
awal = 0
a = int(input("Masukan Banyaknya angka : "))
for i in range(0, a):
    b = eval(input("Masukan angka : "))
    awal += b
print("jumlah : ",awal)
print("Rata-rata : ", awal / a)

print("\n\n")  #  \n = karakter untuk membuat enter / baris baru

print("contoh 2.2")
print("\n")
awal = 0
a = int(input("Masukan Banyaknya angka : "))
for i in range(0, a):
    b = eval(input("Masukan angka : "))
    awal += b
print("jumlah : ",awal)
print("Rata-rata : ", awal / a)


print("\n\n")

# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini

print("SOAL 3 - Mencetak Persegi ")
print("\n")
x = int(input("masukkan sebuah bilangan bulat : "))
for i in range(x):
    for j in range(x):
        print('#', end=' ')
    print()
