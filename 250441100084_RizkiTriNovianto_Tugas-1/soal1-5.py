print("Soal 1")

text = ("Seorang programer sedang membuat program sederrhana untuk menghitung indeks Prestasi Mahasiswa (IPK). Program tersebut membutuhkan penyimpanan dengan data berikut:")  

print()

print(text)
print()

print ("\u2022 Nama lengkap mahasiswa : Rizki Tri Novianto")
print ("\u2022 Nomor Induk Mahasiswa (NIM) : 250441100084")

a = 20
print ("\u2022 Jumlah SKS :",a)

b = 3.8 

if b > 3:
    status_aktif =True

else: 
    status_aktif =False
    
if status_aktif == True:
    print ("\u2022 Status Keaktifan : Aktif")
else: 
    print ("\u2022 Status Keaktifan : Tidak Aktif")

print ("\u2022 IPK saat ini :",b)

print()
print ("Soal 2")
print()
jumlah_barang =  "5"

harga_satuan = 15000

total_sementara = jumlah_barang * 2 

print("Total sementara:", total_sementara)


jumlah_barang = int(jumlah_barang) 

total_akhir = jumlah_barang * harga_satuan
print("Total akhir:", total_akhir)

print()
print("Soal 3")
print()

hasil = 10 + 5 * 2 - 12 / 6 % 3
print(hasil)

print()
print("Soal 4")
print()


print("Kriteria Lulus Tepat Waktu :")

masa_studi = 5
IPK = 3.8
ada_nilai_e = False

if (masa_studi <= 8) and (IPK >= 3.00) and (ada_nilai_e == False):
    print("Lulus Tepat Waktu")
else:
    print("Tidak Lulus Tepat Waktu")

