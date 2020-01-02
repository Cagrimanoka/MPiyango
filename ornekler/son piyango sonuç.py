from mpiyango import sonuclar,tarihler
from mpiyango import piyango as p

bilet_no = 1234567

tarih = int(tarihler(p)[0])             #Son piyango çekilişinin tarihini alır.
sonuc = sonuclar(p, tarih)              #Piyango verilerini TopSonuc sınıfı altında depolar.

print(sonuc.ikr_ve_num())               #İkramiye çıkan numaraları ve çıkan miktarları sözlük olarak verip yazdırır.
print(sonuc.biletkontrol(bilet_no))     #Verilen bilet numarasına çıkan ikramiyeyi verir.
print(sonuc.il_ilce)                    #Biletin çıktığı ilçe/ili yazdırır.