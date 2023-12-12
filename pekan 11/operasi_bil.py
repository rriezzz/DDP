import math

def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print("Hasil penjumlahan dari",bil1, "+", bil2, "adalah:", hasil)

def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print("Hasil pengurangan dari",bil1, "-", bil2, "adalah:", hasil)

def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("Hasil perkalian dari",bil1, "x", bil2, "adalah:", hasil)

def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print("Hasil bagi dari",bil1, "/", bil2, "adalah:", hasil)

def pangkat(bil1, bil2):
    hasil = bil1 ** bil2
    print("Hasil pangkat dari",bil1, "**", bil2, "adalah:", hasil)

def modulus(bil1, bil2):
    hasil = bil1 % bil2
    print("Sisa hasil dari pembagian",bil1, "/", bil2, "adalah:", hasil)

def pecahan(bil1, bil2):
    hasil1 = bil1 // bil2
    hasil2 = bil1 % bil2
    print("Hasil pecahan dari pembagian",bil1, "/", bil2, "adalah:",'{} {}/{}'.format(hasil1, hasil2, bil2))

def pembagian_bulat(bil1, bil2):
    hasil = bil1 // bil2
    print("Hasil dari pembagian bulat",bil1, "//", bil2, "adalah:", hasil)

def log10(bil1):
    hasil = math.log10(bil1)
    print("Hasil dari",bil1, "log10 adalah :", hasil)

def akar(bil1):
    hasil = math.sqrt(bil1)
    print("Hasil akar pangkat 2 dari",bil1, "adalah :", hasil)


