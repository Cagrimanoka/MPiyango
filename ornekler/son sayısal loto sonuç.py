from mpiyango import sonuclar, tarihler
from mpiyango import sayisal as s

tarih = int(tarihler(s)[0])             #Son Sayısal Loto çekilişinin tarihini alır.
sonuc = sonuclar(s, tarih)              #Sayısal Loto verilerini TopSonuc sınıfı altında depolar.

print(sonuc.devird())                   #İkramiyenin devir verilerini yazdırır.
print(sonuc.sonuc)                      #Çıkan rakamların listesini yazdırır.
print(sonuc.b_liste())                  #Bilen verilerini (kişi başı ikramiye vs.) sözlük halinde verir.