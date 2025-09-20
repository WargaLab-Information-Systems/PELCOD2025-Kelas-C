# print("Kalkulator Cringe")
# angka1 = float(input("Masukkan angka pertama: "))
# operator = input("Masukkan (+ - * /): ")
# angka2 = float(input("Masukkan angka kedua: "))

# if operator == "+":
#     hasil = angka1 + angka2
# elif operator == "-":
#     hasil = angka1 - angka2
# elif operator == "*":
#     hasil = angka1 * angka2
# elif operator == "/":
#     hasil = angka1 / angka2
# else:
#     hasil = "Operator tidak valid"

# print("Hasil:", hasil)


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

