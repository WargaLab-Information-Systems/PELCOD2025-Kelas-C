jumlah_barang = "5" 
harga_satuan = 15000
total_sementara = jumlah_barang * 2
print("Total sementara:", total_sementara)

jumlah_barang = int(jumlah_barang) 
total_akhir = jumlah_barang * harga_satuan
print("Total akhir.",total_akhir)


# mendefenisikan variabel untuk mengecek kriteria kelulusan 
masa_studi = 7
ipk = 3.00
ada_nilai_e = False

print((masa_studi <= 8) and (ipk >= 3.00) and (ada_nilai_e ==False))
