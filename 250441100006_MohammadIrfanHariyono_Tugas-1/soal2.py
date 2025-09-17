soal2 = "Perhatikan potongan kode dalam bahasa Python berikut:"
print(soal2)

print()

jumlah_barang = "5"
harga_satuan = 15000
total_sementara = jumlah_barang * 2
print("Total Sementara : ", total_sementara)

jumlah_barang = int(jumlah_barang)
total_akhir = jumlah_barang * harga_satuan
print("Total akhir : ", total_akhir)

#JAWABAN

#Output yang di hasilkan adalah 55 karena jumlah barang berupa type data string yaitu = “5” sedangkan adanya “” adalah dimana type data String di pakai jadi python meresponya bahwa angka tersebut harus diulang,
#lalu mengapa hasilnya bisa 55 karena adanya variabel di bawahnya dimana Total_sementara = jumlah_barang * 2 atau bisa dibilang dikali berhubung variabel di atas menggunakan string maka python meresponya dengan pemunculan secara 2 kali maka jadilah angka 55,
#lalu lanjut ke total akhir ada perubahan variabel dari yang awalnya tipe data string di rubah menjadi integer(int) saat sebelum penghitungan pada total_akhir