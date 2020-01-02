from mpiyango import sonuclar,tarihler
from mpiyango import cekilis_turleri as t


tarih = int(tarihler(t.sayisal)[0])     #Son Sayısal Loto çekilişinin tarihini alır.
sonuc = sonuclar(t.sayisal, tarih)      #Sayısal Loto verilerini TopSonuc sınıfı altında depolar.

print(sonuc.devird())                   #İkramiyenin devir verilerini yazdırır.
print(sonuc.sonuc)                      #Çıkan rakamların listesini yazdırır.
print(sonuc.b_liste())                  #Bilen verilerini (kişi başı ikramiye vs.) sözlük halinde verir.

input()