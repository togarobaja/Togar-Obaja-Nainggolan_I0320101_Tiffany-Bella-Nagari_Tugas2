#TOGAR OBAJA NAINGGOLAN
#NIM I0320103
#KELAS C
#Soal 1

#Menghitung Luas
print("Menghitung Luas Lingkaran")
r = float(input("masukkan jari-jari yang diinginkan :"))
Ll = 3.14 * (r ** 2)
print("Luas Lingkaran :", Ll)

print("Menghitung Luas Persegi Panjang")
p = float(input("masukkan nilai panjang: "))
l = float(input("masukkan nilai lebar: "))
Lp= p * l
print("Luas Persegi Panjang: ", Lp)

print("Menghitung Luas Kubus")
s = float(input("masukkan nilai sisi : "))
Lk = 6 * (s ** 2)
print("Luas kubus :", Lk)

#Menghitung Konversi Suhu
print("Konversi suhu Celcius ke Fahrenheit")
C = float(input("masukkan suhu Celcius : "))
F = C * 9 / 5 + 32
print("Celcius : ", C)
print("Fahrenheit : ", F)

print("Konversi suhu Reamur ke Kelvin")
R = float(input("masukkan suhu Reamur : "))
K = R / 4 * 5 + 273
print("Reamur : ", R)
print("Kelvin : ", K)