# program menghitung ipk mahasiswa
# input data mahasiswa

nama = input("masukkan nama lengkap mahasiswa: ")  #str krn bilangan bulat
nim = input(" masukkan nim: ") #str krn bilangn bulat
sks = int(input("masukkan jumlah sks yang diambil: ")) #int krn bilangn bulat
status_input = input("masukkan status keaktifan (ya/tidak): ")
status = True if status_input == "ya" else False  #bool  krn mudah
ipk = float(input("masukkan ipk saat ini: "))  #float krn desimal

# output data mahasiwa
print("\n=== Data Mahasiswa ===")
print("nama lengkap   :", nama)
print("nim            :", nim)
print("jumlah sks     :", sks)
print("status aktif   :", "aktif" if status else "tidak aktif")
print("ipk saat ini   :", ipk)