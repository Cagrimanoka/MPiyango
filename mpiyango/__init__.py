import requests
import json
from ast import literal_eval

OYUN_SAYISI = 5

class Turler:
    def __init__(self):
        self.piyango = 0
        self.sanstopu = 1
        self.onnumara = 2
        self.sayisal = 3
        self.superloto = 4


cekilis_turleri = Turler()

turler = [cekilis_turleri.piyango, cekilis_turleri.sanstopu, cekilis_turleri.onnumara, cekilis_turleri.sayisal, cekilis_turleri.superloto]
tur_linkler = ["piyango", "sanstopu", "onnumara", "sayisal", "superloto"]
tur_isimler = ["Milli Piyango", "Şans Topu", "On Numara", "Sayısal Loto", "Süper Loto"]

class Tarih:
    def __init__(self, jsonformat, o_format):
        self.jsonformat = int(jsonformat)
        self.o_format = o_format
    def __str__(self):
        return self.o_format
    def __repr__(self):
        return self.jsonformat
    def __int__(self):
        return self.jsonformat

class IlIlce:
    def __init__(self, il, ilce):
        self.il = il
        self.ilce = ilce
    def __str__(self):
        return f"{self.ilce}/{self.il}"
    def __repr__(self):
        return f"{self.ilce}/{self.il}"

class Devir:
    def __init__(self, devir, sayi, tutar):
        self.devir = devir
        self.sayi = int(sayi)
        if not sayi:
            self.tutar = 0
        else:
            self.tutar = float(tutar)
    def __int__(self):
        return self.tutar
    def d(self):
        return {"devir":self.devir, "devir_sayisi":self.sayi, "devir_tutari":self.tutar}

class Bilen:
    def __init__(self, kisi_basi_ikr, kisi, tur):
        self.kisibasi = float(kisi_basi_ikr)   #Kişi başına düşen ikramiye
        self.kisi = int(kisi)                  #Bilen kişi sayısı
        self.tur = tur                         #Tür
    def d(self):
        return {"ikramiye": self.kisibasi, "kisi_sayi": self.kisi, "tur": self.tur}

class PiyangoHaneSonuc:
    def __init__(self, numaralar, ikramiye, tip, hanesayisi):
        self.numaralar = sorted(numaralar)
        self.ikramiye = float(ikramiye)
        self.tip = tip
        self.hanesayisi = int(hanesayisi)
    def num_ikr(self):
        return {"ikramiye":self.ikramiye, "numaralar":self.numaralar}
    def numarakontrol(self, numara):
        numara = str(numara)
        if self.hanesayisi > len(numara):
            raise Exception("Hatalı numara - Bilet numarası hane sayısını kontrol edin!")
        if self.hanesayisi != 0 and self.hanesayisi < len(numara):
            if numara[self.hanesayisi * (-1):] in self.numaralar:
                return self.ikramiye
            else:
                return 0
        else:
            if numara in self.numaralar:
                return self.ikramiye
            else:
                return 0

class PiyangoSonuc:
    """Piyango çekilişinin sonucu ve bilgileri"""
    def __init__(self, json_str):
        self.j_data = json_str
        self.tur = cekilis_turleri.piyango
        self.tur_str = tur_isimler[cekilis_turleri.piyango]
        s_dict = json.loads(json_str)
        self.ad = s_dict["cekilisAdi"]
        self.tarih = Tarih(s_dict["cekilisTarihi"], f"{s_dict['cekilisTarihi'][0:4]}/{s_dict['cekilisTarihi'][4:6]}/{s_dict['cekilisTarihi'][6:8]}")
        self.hane_sayisi = int(s_dict["haneSayisi"])
        self.sonuclar = [PiyangoHaneSonuc(i["numaralar"], i["ikramiye"], i["tip"], i["haneSayisi"]) for i in s_dict["sonuclar"]]
        self.il_ilce = [IlIlce(i["ilView"], i["ilceView"]) for i in s_dict["buyukIkrKazananIlIlceler"]]
    def biletkontrol(self, numara):
        """Numaraya ödül çıkıp çıkmadığını kontrol eder, çıkmışsa çıkan en yüksek miktarı değer olarak verir, çıkmamışsa 0 verir."""
        return max([sonuc.numarakontrol(numara) for sonuc in self.sonuclar])
    def ikr_ve_num(self):
        """İkramiyelerle birlikte numaraları verir."""
        return [i.num_ikr() for i in self.sonuclar]

class SansTopuSonuc:
    """Şans Topu çekilişinin sonucu ve bilgileri"""
    def __init__(self, json_str):
        self.j_data = json_str
        self.tur = cekilis_turleri.sanstopu
        self.tur_str = tur_isimler[cekilis_turleri.sanstopu]
        s_dict = json.loads(json_str)
        if not s_dict["success"]:
            raise Exception("Bir hata oluştu -  Veri alımı başarısız oldu!")
        else:
            data = s_dict["data"]
            self.hafta = int(data["hafta"])
            self.tarih = Tarih("".join(data["cekilisTarihi"].replace("-","/").split("/")[::-1]), data["cekilisTarihi"])
            rkm = [int(i) for i in data["rakamlar"].split("#")]
            self.rakamlar = sorted(rkm[:-1]) + rkm[-1:]
            self.sanslirakam = rkm[-1:]
            self.sonuc = self.rakamlar
            self.devir = Devir(data["devretti"], data["devirSayisi"], data["haftayaDevredenTutar"])
            self.hasilat = float(data["hasilat"])
            self.ikramiye = float(data["ikramiyeEH"])
            self.bilenler = [Bilen(i["kisiBasinaDusenIkramiye"], i["kisiSayisi"], i["tur"]) for i in data["bilenKisiler"]]
            self.il_ilce = [IlIlce(i["ilView"], i["ilceView"]) for i in data["buyukIkrKazananIlIlceler"]]
    def devird(self):
        """Devir verilerini sözlük elemanı olarak verir."""
        return self.devir.d()
    def b_liste(self):
        """Bilen verilerini (kişi başı ikramiye vs.) sözlük olarak verir"""
        return [bilen.d() for bilen in self.bilenler]

class TopSonuc:
    """Diğer çekilişlerin sonuçları ve bilgileri"""
    def __init__(self, json_str, tur):
        self.j_data = json_str
        self.tur = tur
        self.tur_str = tur_isimler[tur]
        s_dict = json.loads(json_str)
        if not s_dict["success"]:
            raise Exception("Bir hata oluştu -  Veri alımı başarısız oldu!")
        else:
            data = s_dict["data"]
            self.hafta = int(data["hafta"])
            self.tarih = Tarih("".join(data["cekilisTarihi"].replace("-","/").split("/")[::-1]), data["cekilisTarihi"])
            self.rakamlar = sorted([int(i) for i in data["rakamlar"].split("#")])
            self.sonuc = self.rakamlar
            self.devir = Devir(data["devretti"], data["devirSayisi"], data["haftayaDevredenTutar"])
            self.hasilat = float(data["hasilat"])
            self.ikramiye = float(data["ikramiyeEH"])
            self.bilenler = [Bilen(i["kisiBasinaDusenIkramiye"], i["kisiSayisi"], i["tur"]) for i in
                             data["bilenKisiler"]]
            self.il_ilce = [IlIlce(i["ilView"], i["ilceView"]) for i in data["buyukIkrKazananIlIlceler"]]

    def devird(self):
        """Devir verilerini sözlük olarak verir."""
        return self.devir.d()
    def b_liste(self):
        """Bilen verilerini (kişi başı ikramiye vs.) sözlük olarak verir"""
        return [bilen.d() for bilen in self.bilenler]



def tarihler(tur):
    """Verilen türdeki çekilişin www.mpi.gov.tr sitesinde sonuçları olan tarihlerini "Tarih" sınıfı içerisinde verir."""
    trh = literal_eval(requests.get(f"http://www.mpi.gov.tr/sonuclar/listCekilisleriTarihleri.php?tur={tur_linkler[tur]}").text[1:])
    return [Tarih(i["tarih"], i["tarihView"]) for i in trh]

def sonuclar(tur, tarih):
    """Verilen türdeki çekilişin verilen tarihteki sonucunu verir. Tarihler "Tarih" sınıfı ile verilmediyse YYYYAAGG formatında olmalıdır."""
    if hasattr(tarih, "jsonformat"):
        tarih = tarih.jsonformat
    else:
        tarih = int(tarih)
    if tur != cekilis_turleri.sayisal:
        snc = requests.get(f"http://www.mpi.gov.tr/sonuclar/cekilisler/{tur_linkler[tur]}/{tarih}.json")
    else:
        snc = requests.get(f"http://www.mpi.gov.tr/sonuclar/cekilisler/{tur_linkler[tur]}/SAY_{tarih}.json")
    snct = snc.text
    if not snct.startswith("{"):
        if tur != cekilis_turleri.sayisal: # Milli Piyango 30.06.2018 ve önceki Sayısal Loto çekilişleri için eski format link kullandığı için
            raise Exception("Geçersiz tarih - Tarihi kontrol edin!")
        else:
            snc = requests.get(f"http://www.mpi.gov.tr/sonuclar/cekilisler/{tur_linkler[tur]}/{tarih}.json")
            snct = snc.text
            if not snct.startswith("{"):
                raise Exception("Geçersiz tarih - Tarihi kontrol edin!")
    else:
        if tur == cekilis_turleri.piyango:
            return PiyangoSonuc(snct)
        elif tur == cekilis_turleri.sayisal:
            return SansTopuSonuc(snct)
        elif tur in range(OYUN_SAYISI):
            return TopSonuc(snct, tur)
        else:
            raise Exception("Geçersiz tür!")
