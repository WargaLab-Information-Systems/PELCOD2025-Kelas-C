jumlah_barang="5"#bertipe data string
harga_satuan = 15000
total_sementara = jumlah_barang*2
print("total sementara : ",total_sementara)
#total sementara ber-value hanya jumlah barang *2
#menghasilkan output dengan menggandakan variabel jumlah_barang yang bertipe data string sesuai total perkaliannya

jumlah_barang = int(jumlah_barang)#mengubah tipe data yang sebelumnya string menjadi bilangan bulat(integer)
total_akhir = jumlah_barang*harga_satuan
print("total akhir = ",total_akhir)
#menghasilkan output  total stok barang dan harga nya
# perbedaan total semetara dan total akhir adalah 
# jumlah barang pada total sementara masih menggunkan tipe data string
# sedanglan jumlah barang  pada total akhir sudah di ubah menjadi integer  