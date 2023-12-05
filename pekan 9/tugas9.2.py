buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
def balikan(daftar_buah):
    buah_terbalik = []
    for buah in reversed(daftar_buah):
        buah_terbalik.append(buah)
    return buah_terbalik


hasil_balikin = balikan(buah)
print(hasil_balikin)
