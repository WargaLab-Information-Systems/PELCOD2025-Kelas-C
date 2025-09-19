print("Soal 1")

Tulisan = ("Seorang Programmer sedang membuat program sederhana untuk menghitung Indeks Prestasi Mahasiswa (IPK). Program tersebut membutuhkan penyimpanan data berikut : ")

print()

print(Tulisan)
print()

print("\u2022 Nama Lengkap Mahasiswa : Moh. Umar Faruq")
print("\u2022 Nomor Induk Mahasiswa (NIM) : 250441100120")

sks = 20
print("\u2022 Jumlah SKS :",sks)

ipk = 3.9
if ipk > 2 :
    status_aktif = True

else :
    status_aktif = False

if status_aktif == True :
    print ("\u2022 status keaktifan : aktif")
else :
    print("\u2022 status keaktifan : tidak aktif")

print("\u2022 IPK saat ini :",ipk)

Tulisan = ("Jawab")

print(Tulisan)

a = ("String : Karena menggunakan huruf dan Spasi pada serangkaian karakter atau pada sebuah kata atau syntex.") 
b = ("String : karena NIM adalah serangkaian karakter yang terdiri dari angka dan tidak digunakan untuk perhitungan matematika, atau lebih tepatnya disimpan sebagai text.")
c = ("Integer : Karena SKS menunjukkan bilangan bulat ( seperti 1,2,3 ) yang tidak memilki bagian desimal atau  pecahan. ")
d = ("Boolean(True/False) : Karena menunjukkan kondisi data tersebut aktif atau tidak aktif yang hanya memiliki dua Kemungkinan nilai yaitu benar ( True ) atau salah ( False).  ")
e = ("Float : Kerena IPK menunjukkan bilangan pecahan, yang ditandai dengan tanda koma sebagai penampungan angka dibelakang koma desimal.")

print(a)
print(b)
print(c)
print(d)
print()

print()
print("Soal 2")
print()

jumlah_barang = "5"
harga_satuan = 15000
total_sementara = jumlah_barang * 2
print("Total sementara:",total_sementara)

jumlah_barang = int(jumlah_barang)
total_akhir = jumlah_barang * harga_satuan
print("Total akhir:",total_akhir)

Tulisan = ("Jawab")

print(Tulisan)
print()

a = ("output yang di hasilkan adalah 55 untuk total sementara sedangkan total  akhir adalah 75000 , kenapa menghasilkan 55 karan jumlah barang = mengugunakan tanda petik “5” sedangkan adanya  tanda petik (“”) adalah diunakan pada tipe data String. jadi python meresponya bahwa angka tersebut harus diulang lalu mengapa hasilnya bisa 55 karena jumlah barang tersebut termasuk menggunakan tipe data string yaitu Total_sementara = jumlah_barang * 2 atau bisa dibilang dikali 2 pengulangan angka yang sama, berhubung variabel di atas menggunakan string maka python meresponya dengan pemunculan secara 2 kali maka jadilah angka 55 lalu lanjut ke total akhir, didalam total akhir ada perubahan varibel dari yang awalnya tipe data string di rubah menjadi integer(int) saat sebelum penghitungan pada total_akhir, maka total_akhir = jumlah_barang *harga satuan maka hasilnya 75000.")

print(a)
print()

print()
print("Soal 3")
print()

hasil = 10 + 5 * 2 - 12 / 6 % 3
print(hasil)

Tulisan = ("Jawab")

print(Tulisan)
print()

a = ("Hasil = 10 + 5 * 2 – 12 / 6 % 3")
b = ("      = 10 + 10 – 12 / 6 % 3")
c = ("      = 10 + 10 – 2 % 3")
d = ("      = 10 + 10 – 2")
e = ("      = 20-2")
f = ("      = 18")

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print()
a = ("Mengapa hasilnya 18 karna dalam aritmatika yang dikerjakan terlebih dahulu adalah Perkalian, pembagian, modulus, penjumlahan dan pengurangan")
print(a)
print()


print()
print("Soal 4")

Tulisan = ("Buatlah satu baris ekspresi logika (dalam pseudocode) yang akan menghasilkan nilai True jika mahasiswa memenuhi syarat, dan False jika tidak.")

print()

print(Tulisan)
print()

print("Kriteria Lulus Tepat Waktu :")

masa_studi = 6
IPK = 3.9
ada_nilai_e = False

if (masa_studi <= 8) and (IPK >= 3.00) and (ada_nilai_e == False):
    print("Lulus Tepat Waktu")
else :
    print("Tidak Lulus Tepat Waktu")


print()
print("Kriteria Tidak Lulus Tepat Waktu :")

masa_studi = 9
IPK = 2.5
ada_nilai_e = True

if (masa_studi <= 8) and (IPK >= 3.00) and (ada_nilai_e == True):
    print("Lulus Tepat Waktu")
else :
    print("Tidak Lulus Tepat Waktu")
print()

Tulisan = ("Jawab")

print(Tulisan)
print()

c = ("Mengapa yang pertama menunjukkan Lulus tepat waktu karna semua kriterianya memenuhi syarat sedangkan yang kedua tidak memenuhi syarat maka hasilnya tidak lulus tepat waktu. Mengapa cara tersebut menggunakan operator and karna jika salah satu tidak sesuai dengan syarat maka hasilnya akan bernilai false tapi jika semuanya sesuai syarat maka hasilnya bernilai true.")

print(c)
