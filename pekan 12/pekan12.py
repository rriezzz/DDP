#procedural
#nasabah1_nama = "Riz"
#nasabah1_norek = "0111"
#nasabah1_saldo = 50000

#nasabah2_nama = "ado"
#nasabah2_norek = "0101"
#nasabah2_saldo = 70000

#print(nasabah1_nama)
#print(nasabah1_norek)
#print(nasabah1_saldo)

class Bank:
    # variabel member 1
    norek = ''
    nama = ''
    saldo = 0
    jmlNasabah = 0 # variabel statis
    BANK = 'Bank Syariah Penghuni Jannah' # variabel konstanta

    # member 2 konstruktor
    # konstruktor akan jalan otomatis berjalan ketika class dipanggil
    def __init__(self, no, nasabah, saldo):
        self.norek = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.jmlNasabah += 1

    # member 3 method
    def nabung(self, uang):
        #self.saldo = self.saldo + uang
        self.saldo += uang
    
    def tarik(self, uang):
        self.saldo -= uang

    def cetak(self): print(Bank.BANK,
    '\n==========================',
    '\nNo. Rekening\t:',self.norek,
    '\nNama Nasabah\t:',self.nama,
    '\nSaldo\t\t: Rp. ',format(self.saldo, ','), '\n--------------------------'
    )
        
nasabah1 = Bank("1001", "Aldi", 50000)
nasabah2 = Bank("1002", "Edo", 70000)

nasabah1.nabung(4000)
print(nasabah2.norek)