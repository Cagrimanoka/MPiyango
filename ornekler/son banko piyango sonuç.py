from mpiyango import sonuclar,tarihler
from mpiyango import cekilis_turleri as t


bilet_no = "09262"

tarih = int(tarihler(t.bankopiyango)[0])     #Son piyango çekilişinin tarihini alır.
sonuc = sonuclar(t.bankopiyango, tarih)      #Piyango verilerini TopSonuc sınıfı altında depolar.

print(sonuc.ikr_ve_num())               #İkramiye çıkan numaraları ve çıkan miktarları sözlük olarak verip yazdırır.
print(sonuc.biletkontrol(bilet_no))     #Verilen bilet numarasına çıkan ikramiyeyi verir.
print(sonuc.il_ilce)                    #Biletin çıktığı ilçe/ili yazdırır.

input()