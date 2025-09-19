jumlah_barang = "5"
harga_satuan = 15000
total_sementara = jumlah_barang * 2
print("Total_sementara:", total_sementara)

jumlah_barang = int(jumlah_barang)
total_akhir = jumlah_barang * harga_satuan
print("Total_akhir:", total_akhir)


# PENJELASAN
# SOAL NO.1 apa output yang akan di hasilkan pada kode di atas?
# jawban:
# total_sementara: 55
# total_akhir: 75000
# SOAL NO.2 jelaskan mengapa outputnya seperti iitu, terutama perbedaan antara total_sementara dan total_akhir
# jawaban:
# total_sementara menghasilkan 55 karena jumlah_barang = "5" memiliki nilai string, yang dimana dlam pengoperasian python jika string * integer akan menghasilkan pengulangan string. (string "5" * 2) menghasilkan 55 
# total_akhir mengasilkan 75000 karena jumlah_barang = 5 memiliki nilai integer, yang berari operasi matematika umum akan berjalan bagaimana semestinya. (5 * 15000) menghasilkan 75000