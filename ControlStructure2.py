angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

if angka1 > angka2 and angka1 > angka3:
    largest = angka1
    print("Angka terbesar adalah:", largest)
elif angka2 > angka1 and angka2 > angka3:
    largest = angka2
    print("Angka terbesar adalah:", largest)
elif angka3 > angka1 and angka3 > angka2:
    largest = angka3
    print("Angka terbesar adalah:", largest)
else:
    print("Tidak ada angka terbesar")