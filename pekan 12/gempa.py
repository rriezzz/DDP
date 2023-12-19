class Gempa:
    lokasi = ''
    besarSkala = ''
    
    def __init__(self, tkp, skala):
        self.lokasi = tkp
        self.besarSkala = skala
        
    def dampak(self):
        if self.besarSkala < 2 :
            print(f"Dampak gempa yang terjadi di {self.lokasi} dengan magnitudo {self.besarSkala} sr : tak terasa")
        elif 2 <= self.besarSkala < 4 :
            print(f"Dampak gempa yang terjadi di {self.lokasi} dengan magnitudo {self.besarSkala} sr : bangunan retak-retak")
        elif 4 <= self.besarSkala < 6 :
            print(f"Dampak gempa yang terjadi di {self.lokasi} dengan magnitudo {self.besarSkala} sr : bangunan roboh")
        elif self.besarSkala >= 6 :
            print(f"Dampak gempa yang terjadi di {self.lokasi} dengan magnitudo {self.besarSkala} sr : bangunan hancur dan potensi tsunami")
        else:
            print("Nilai Skala tidak valid!")

pertama = Gempa("Banten", 1.2)
kedua = Gempa("Palu", 6.1)
ketiga = Gempa("Cianjur", 5.6)
keempat = Gempa("Jayapura", 3.3)
kelima = Gempa("Garut", 4.0)