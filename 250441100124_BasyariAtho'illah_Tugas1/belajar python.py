


print("Yuk cek apakah kamu mahasiswa tepat waktu!")

masa_studi = int(input("Masukkan Berapa semester masa studimu: "))
ipk = float(input("Masukkan IPK: "))
e = input("Apakah anda memiliki nilai E? (ya/tidak) ").lower()
#
if masa_studi > 8:
    print("Kamu Tidak lulus tepat waktu diakernakan masa studimu melebihi 8 semester")

elif ipk < 3.00:
    print("Kamu Tidak lulus tepat waktu dikarenakan IPK kamu dibawah 3.00")

elif e == "ya":
    print("Kamu Tidak lulus tepat waktu dikarenakan ada nilai E di raportmu")

else:
    print("ANJAY LULUS TEPAT WAKTU")

