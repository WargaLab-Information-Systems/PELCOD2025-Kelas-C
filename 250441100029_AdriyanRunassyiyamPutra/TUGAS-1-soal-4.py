masa_studi=int(input("masa studi = "))
ipk=float(input("Input IPK : "))
ada_nilai_e= input("apakah ada nilai e ? ")
nilai=ada_nilai_e

if nilai.lower()=="true":
    ada_nilai_e= True
elif nilai.lower()=="false":
    ada_nilai_e=False

if ada_nilai_e == False and masa_studi <= 8 and ipk >=3.00:
    print("lulus tepat waktu")
elif ada_nilai_e == True or masa_studi >= 8 and ipk<=3.00:
    print("lulus tidak tepat waktu")