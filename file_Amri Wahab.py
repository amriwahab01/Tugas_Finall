# Nama = Amri Wahab
# Nim = D0221332
#kelas = E


class BangunDatar:
    def luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi**2

class Segitiga(BangunDatar):
    def __init__(self,alas,tinggi) :
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return self.alas * self.tinggi / 2

class Lingkaran(BangunDatar):
    def __init__(self,jari2):
        self.phi = 22/7
        self.jari2 = jari2

    def luas(self):
        return self.phi * (self.jari2**2)

class BangunRuang:
    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi**3

class Limas(BangunRuang):
    def __init__(self,panjang_alas,tinggi_alas,tinggi_limas):
        self.panjang_alas = panjang_alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_limas = tinggi_limas

    def volume(self):
        return (self.panjang_alas*self.tinggi_alas/2) * self.tinggi_limas / 3

class Tabung(BangunRuang):
    def __init__(self,jari2,tinggi):
        self.phi = 22/7
        self.jari2 = jari2
        self.tinggi = tinggi

    def volume(self):
        return self.phi * (self.jari2**2) * self.tinggi

def menu():
    while True : 
        print('''=====menu=====
1. persegi
2. segitiga
3. lingkaran
4. kubus
5. limas
6. tabung
4. menu sebelumnya''')
        pilihan = int(input("pilih kode menu diatas : "))
        if pilihan == 1 : 
            print("menghitung luas persegi")
            sisi = int(input("masukkan panjang sisi : "))
            persegi = Persegi(sisi)
            print("luas persegi = ",persegi.luas()) 
        elif pilihan == 2 : 
            print("menghitung luas segitiga")
            alas = int(input("masukkan panjang alas segitiga : "))
            tinggi = int(input("masukkan panjang tinggi segitiga : "))
            segitiga = Segitiga(alas,tinggi)
            print("luas segitiga = ",segitiga.luas())
        elif pilihan == 3 : 
            print("menghitung luas lingkaran")
            jari2 = int(input("masukkan panjang jari-jari : "))
            lingkaran = Lingkaran(jari2)
            print("luas lingkaran = ",int(lingkaran.luas()))
        
            
        elif pilihan == 4 : 
            print("menghitung volume kubus")
            sisi = int(input("masukkan panjang sisi : "))
            kubus = Kubus(sisi)
            print("volume kubus = ",kubus.volume()) 
        elif pilihan == 5 : 
            print("menghitung volume limas segitiga")
            alas = int(input("masukkan panjang alas segitiga : "))
            tinggi_alas = int(input("masukkan panjang tinggi alas segitiga : "))
            tinggi_limas = int(input("masukkan panjang tinggi limas : "))
            limas = Limas(alas,tinggi_alas,tinggi_limas)
            print("volume limas segitiga = ",limas.volume())
        elif pilihan == 6 : 
            print("menghitung volume tabung")
            jari2 = int(input("masukkan panjang jari-jari : "))
            tinggi = int(input("masukkan tinggi tabung : "))
            tabung = Tabung(jari2,tinggi)
            print("volume tabung = ",int(tabung.volume()))
        elif pilihan == 7 : 
            menu_utama()
        else : 
            print("masukkan kode menu dengan benar!")
menu()

        

