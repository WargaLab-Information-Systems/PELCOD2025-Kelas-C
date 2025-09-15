#soal _1
# string karena menggunkan nama
nama_lengkap_mahasiswa = "nama mahasiswa"

# integer karena menggunakan angka
nim = 11111111

# integer karena menggunakan angka
jumlah_sks = 20

# boolean karena hanya ada dua pilihan
mahasiswa_aktif = True
mahasiswa_tidak_aktif = False

# float karena menggunakan angka desimal
ipk = 3.54

# soal_2

jumlah_barang = "5"
harga_satuan = 15000
total_sementara = "5"*2

print("total sementara:", total_sementara)

total_sementara = 55
jumlah_barang = int(jumlah_barang)
total_akhir = jumlah_barang*harga_satuan

print("total akhir:", total_akhir)
total_akhir = 75000
#penjelasan
total_sementara = '55 karena menggunkan string jadi teks 5 di ulang 2'
total_akhir = '75000 karena mengubah jumlah barang dari string ke integer'

# # soal_3
# hasil = 10 + 5 * 2 - 12 / 6 % 3
# # urutan menghitung
# 5*2 = 10
# 12/6 = 2
# 2%3 = 2
# 10+10-2 = 18

# soal_4
def hitung_lulus(ipk, masa_studi, ada_nilai_e):
    lulus_tepat_waktu = (masa_studi <= 8) and (ipk >= 3.00) and (not ada_nilai_e)
    return lulus_tepat_waktu
ipk = 3.00
masa_studi = 8
ada_nilai_e = False

if hitung_lulus(ipk, masa_studi, ada_nilai_e):
    print("Selamat, Anda lulus tepat waktu!")
else:
    print("Maaf, Anda tidak lulus tepat waktu.")