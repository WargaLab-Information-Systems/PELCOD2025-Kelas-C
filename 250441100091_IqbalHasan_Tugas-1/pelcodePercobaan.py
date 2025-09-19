#SOAL NOMER 2
jumlah_barang = "5"
harga_satuan = 15000
total_sementara = jumlah_barang * 2
print("total sementara:", total_sementara)

jumlah_barang = int(jumlah_barang)
total_akhir = jumlah_barang * harga_satuan
print("total akhir:",total_akhir)


#SOAL NOMER 3
hasil = 10 + 5 * 2 - 12 / 6 % 3
print("Hasil akhir:", hasil)



#SOAL NOMER 4
data_mahasiswa = [
    {"nama": "Aisom", "masa_studi": 9, "ipk": 3.0, "ada_nilai_e": False},
    {"nama": "Dandy", "masa_studi": 7, "ipk": 1.9, "ada_nilai_e": False},
    {"nama": "Reza", "masa_studi": 5, "ipk": 3.6, "ada_nilai_e": True},
    {"nama": "Aji",  "masa_studi": 4, "ipk": 3.8, "ada_nilai_e": False},
]

for data in data_mahasiswa:
    if (data["masa_studi"] <= 8) and (data["ipk"] >= 3.0) and (not data["ada_nilai_e"]):
        print(data["nama"], "= Lulus Tepat Waktu")
    else:
        print(data["nama"], "Tidak Lulus Tepat Waktu")
