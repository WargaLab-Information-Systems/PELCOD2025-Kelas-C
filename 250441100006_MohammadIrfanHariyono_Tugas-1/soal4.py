soal4 = "Buatlah satu baris ekspresi logika (dalam pseudocode) yang akan menghasilkan nilai True jika Mahasiswa memenuhi syarat, dan false jika tidak, gunakan variabel masa_studi (integer), ipk (float), dan ada_nilai_e (boolean)."

masa_studi = 8
ipk = 3.00
tidak_ada_nilai_e = True
ada_nilai_e = True
if masa_studi <= 8:
    tidak_ada_nilai_e = True
else:
    tidak_ada_nilai_e = False

if tidak_ada_nilai_e == True:
    print("Mahasiswa memenuhi syarat : Lulus tepat waktu")
else:
    print("Mahasiswa tidak memenuhi syarat : Lulus tidak tepat waktu")

if masa_studi >= 8:
    ada_nilai_e = True
else:
    ada_nilai_e = False

if ada_nilai_e == False:
    print("Mahasiswa memenuhi syarat : Lulus tepat waktu")
else:
    print("Mahasiswa tidak memenuhi syarat : Lulus tidak tepat waktu")

#JAWABAN

#Pseudocode

#Memenuhi syarat :
#(masa_studi <= 8) AND (ipk >= 3.00) AND (ada_nilai_e == False) 
#, Jika tidak memenuhi syarat :
#(masa_studi >=8) AND (ipk <= 3.00) AND (ada_nilai_e == True)
