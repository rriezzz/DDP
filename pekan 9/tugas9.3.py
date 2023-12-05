buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']



def duplikasi(daftar_buah):
    duplikat = []
    for buah in daftar_buah:
        duplikat.append(buah)
        duplikat.append(buah)
    return duplikat
hasil_duplikat = duplikasi(buah)
print(hasil_duplikat)