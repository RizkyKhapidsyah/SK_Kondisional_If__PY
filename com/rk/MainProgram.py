from pip._vendor.distlib.compat import raw_input

# Created by Rizky Khapidsyah

print("Masukkan dua buah Angka ")
print("Dan kita akan periksa hubungan kedua angka tersebut")

Angka1 = raw_input("Masukkan Angka Pertama : ")
Angka1 = int(Angka1)

Angka2 = raw_input("Masukkan angka kedua : ")
Angka2 = int(Angka2)

if Angka1 == Angka2:
    print("%d sama dengan %d" % (Angka1, Angka2))
if Angka1 != Angka2:
    print("%d tidak sama dengan %d" % (Angka1, Angka2))
if Angka1 < Angka2:
    print("%d kurang dari %d" % (Angka1, Angka2))
if Angka1 > Angka2:
    print("%d lebih dari %d" % (Angka1, Angka2))
if Angka1 <= Angka2:
    print("%d kurang dari sama dengan %d" % (Angka1, Angka2))
if Angka1 >= Angka2:
    print("%d lebih dari sama dengan %d" % (Angka1, Angka2))
