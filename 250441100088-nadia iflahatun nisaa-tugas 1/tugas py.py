# Program Python Sederhana

# Menerima input dari pengguna
nama =input("masukkan nama: ")
umur =int(input("masukkan umur: "))
berat =float(input("masukkah berat (kg): "))
tinggi =float(input("masukkan tinggi (cm): "))


# Operasi Aritmatika
tinggi_meter =tinggi / 100
bbi = berat / (tinggi_meter ** 2)
umur_tahun_depan = umur + 1


# Operasi Logika
cukup_umur = umur >= 16
if bbi < 19:
   kategori_bbi = "langsing"
elif bbi <= 25:
   kategori_bbi = "ideal"
elif bbi <= 30:
   kategori_bbi = "berat badan berlebihan"
else:
   kategori_bbi = "obesitas"

# Output
print("hasil")
print("hai," , nama)
print("umur kamu sekarang:", umur, "tahun")
print("tahun depan umur kamu:", umur + 1, "tahun" )
print("berat badan:", berat, "kg")
print("tinggi badan:", tinggi, "kg")
print("kategori bbi:", kategori_bbi)