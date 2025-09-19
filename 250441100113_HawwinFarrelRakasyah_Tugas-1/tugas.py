#SOAL NO 2

jumlah_barang = 5
harga_satuan = 15000
total_sementara = jumlah_barang * 2
print("total sementara : ", total_sementara)

jumlah_barang = int(jumlah_barang)
total_akhir = jumlah_barang * harga_satuan
print("total akhir : ", total_akhir)

#SOAL NO 4

def lulus_tepat_waktu(masa_studi, ipk, punya_nilai_E):
    if masa_studi <= 8 and ipk >= 3.00 and not punya_nilai_E:
        return "Lulus Tepat Waktu"
    else:
        return "Tidak Lulus Tepat Waktu"

# Contoh penggunaan:
semester = 8
ipk = 3.25
punya_nilai_E = False

status = lulus_tepat_waktu(semester, ipk, punya_nilai_E)
print(status)  # Output: Lulus Tepat Waktu

