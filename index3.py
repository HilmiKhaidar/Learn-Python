a = 10
b = 5

print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian bulat:", a // b)
print("Sisa bagi:", a % b)
print("Pangkat:", a ** b)

umur = int(input("Masukkan umur kamu: "))
punya_ktp = input("Apakah kamu punya KTP? (ya/tidak): ")

boleh_buat_sim = umur >= 17 and punya_ktp.lower() == "ya"

print("Boleh buat SIM C:", boleh_buat_sim)
