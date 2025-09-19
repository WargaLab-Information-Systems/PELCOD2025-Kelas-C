jumlah_barang = "5"
harga_satuan = 15000
jumlah_barang = int(jumlah_barang)
total_sementara = jumlah_barang * 2
print("total sementara:", total_sementara)


total_akhir = jumlah_barang * harga_satuan
print("total akhir:", total_akhir)

# operasi aritmatika
hasil = 10 + 5 * 2 - 12 / 6 % 3
print("hasil dari 10 + 5 * 2 - 12 / 6 % 3 adalah:", hasil)

# data mahasiswa
data_mahasiswa = [
    {"nama": "Mita", "masa_studi": 8, "ipk": 3.3, "ada_nilai_e": False},
    {"nama": "Ilham", "masa_studi": 9, "ipk": 3.5, "ada_nilai_e": False},
    {"nama": "Indri", "masa_studi": 7, "ipk": 2.7, "ada_nilai_e": False},
    {"nama": "Anin", "masa_studi": 6, "ipk": 3.6, "ada_nilai_e": True},
    {"nama": "Fatma", "masa_studi": 7, "ipk": 3.9, "ada_nilai_e": False},
]

# pengecekan lulus tepat waktu
for mhs in data_mahasiswa:
    if (mhs["masa_studi"] <= 8) and (mhs["ipk"] >= 3.0) and (not mhs["ada_nilai_e"]):
        print(mhs["nama"], "= Lulus Tepat Waktu")
    else:
        print(mhs["nama"], "= Tidak Lulus Tepat Waktu")
