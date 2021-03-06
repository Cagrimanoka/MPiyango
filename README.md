
# Python için MPİ Çekiliş Veri Kütüphanesi
`mpiyango` modülü Milli Piyango İdaresi internet sitesinden istenen çekiliş verilerini alarak Python ile işlenebilir hale getirir. Çekilişlerin tarihlerini ve sonuçlarını siteden alabilir.

### Hangi Çekilişler?
1. Milli Piyango
2. On Numara
3. Sayısal Loto
4. Süper Loto
5. Şans Topu
6. Para Loto
7. Süper Piyango
8. Banko Piyango
9. Süper Sayısal Loto
10. Süper Şans Topu
11. Süper On Numara


# Nasıl Kurulur?
    pip install mpiyango

# Örnekler
Basit derecede örnekler için /ornekler konumuna bakabilirsiniz.

# Dokümantasyon (v0.0.9)
## Çekiliş Türleri

 - `mpiyango.cekilis_turleri.piyango` (Piyango)
 - `mpiyango.cekilis_turleri.onnumara` (On Numara)
 - `mpiyango.cekilis_turleri.sayisal` (Sayısal Loto)
 - `mpiyango.cekilis_turleri.superloto` (Süper Loto)
 - `mpiyango.cekilis_turleri.sanstopu` (Şans Topu)
 - `mpiyango.cekilis_turleri.paraloto` (Para Loto)
 - `mpiyango.cekilis_turleri.superpiyango` (Süper Piyango)
 - `mpiyango.cekilis_turleri.bankopiyango` (Banko Piyango)
 - `mpiyango.cekilis_turleri.supersayisal` (Süper Sayısal Loto)
 - `mpiyango.cekilis_turleri.supersanstopu` (Süper Şans Topu)
 - `mpiyango.cekilis_turleri.superonnumara` (Süper On Numara)

## Sınıflar
### `Tarih`

 - **jsonformat** *(int)*: Site tarafından kullanılan tarih formatı (YYYYAAGG) 
 - **o_format** *(str)*: Okunabilir tarih formatı (GG/AA/YYY) (str)

 ### `IlIlce`
- **il** *(str)*: Kazanan il verisi 
- **ilce** *(str)*: Kazanan ilçe verisi
>str olarak kullanılırsa `"İlçe/İl"` stringini verir.

### `Devir`
- **devir** *(bool)*: Devretme durumu
- **sayi** *(int)*:  Devir sayısı
- **tutar** *(float)*: Devreden tutar
- **d()**: {*"devir"*:`devir`, *"devir_sayisi"*:`sayi`, *"devir_tutari"*:`tutar`} sözlüğünü verir.
>int olarak kullanılırsa `tutar` değerini verir.

### `Bilen`
- **kisibasi** *(float)*: Kişi başına düşen ikramiye
- **kisi** *(int)*:  Bilen kişi sayısı
- **tur** *(str)*:Bilinen tür
- **d()**: {*"ikramiye"*:`kisibasi`, *"kisi_sayi"*:`kisi`, *"tur"*:`tur`} sözlüğünü verir.

### `PiyangoHaneSonuc` 
Çekilişteki tek bir ikramiye için sonuçlar.
- **numaralar** *(list)*: Belirtilen ikramiyeyi kazanan numaralar
- **ikramiye** *(float)*:  İkramiye miktarı
- **tip** *(str)*:İkramiye tipi
- **hanesayisi** *(int)*: İkramiye için gereken son n hane. (Eğer tüm numara değilse)
- **num_ikr()**: {*"ikramiye"*:`ikramiye`, *"numaralar"*:`numaralar`} sözlüğünü verir.
- **numarakontrol (`numara(int/str)`)**: Bilet numarası için ikramiye tutuyorsa ikramiyeyi, tutmuyorsa 0 değerini verir.

### `PiyangoSonuc` 
Piyango çekilişinin sonucu ve bilgileri.
- **tur** *(mpiyango.cekilis_turleri.x)*  bkz. **Çekiliş Türleri**
- **tur_str** *(str)*: Çekiliş türü ismi
- **ad** *(str)*: Çekiliş adı (örn. `"19/11/2019 BİLET KONTROL ŞUBE MÜDÜRLÜĞÜ GERÇEK"`)
- **tarih** *(`Tarih`)*: Çekiliş tarihi
- **hanesayisi** *(int)*: Çekiliş hane sayısı
- **sonuclar** *(list[`PiyangoHaneSonuc`])*: Çekiliş sonuçları
 - **il_ilce** *(`IlIlce`)*: Kazanan bilet(ler)in bulunduğu il ve ilçeler
- **biletkontrol (`numara(int/str)`)**: Bilet numarası için ikramiye tutuyorsa tutan en büyük ikramiyeyi, tutmuyorsa 0 değerini verir.
- **ikr_ve_num()**: {*"ikramiye"*:`ikramiye`, *"numaralar"*:`numaralar`} sözlüklerini barındıran bir liste verir.

### `SansTopuSonuc` 
Şans Topu çekilişinin sonucu ve bilgileri.
- **tur** *(mpiyango.cekilis_turleri.x)*  bkz. **Çekiliş Türleri**
- **tur_str** *(str)*: Çekiliş türü ismi
- **hafta** *(int)*:Çekiliş hafta numarası
- **tarih** *(Tarih)*:Çekiliş tarihi
- **rakamlar** *(list[`int`])*: Sondaki rakam şanslı rakam olmak üzere kazanan rakamlar
- **sonuc** *(list[`int`])*: bkz. **rakamlar**
- **sanslirakam** *(int)*: Şanslı rakam
- **devir** *(Devir)*: Devretme verileri
- **hasilat** *(float)*: Elde edilen son hasılat
- **ikramiye** *(float)*: Devirlerle birlikte o haftanın ikramiyesi
- **bilenler** *(list[`Bilen`])*: Listede numaraları bilenlerin istatistikleri
- **il_ilce** *(`IlIlce`)*: Bilen il ve ilçeler
- **devird(`numara(int/str)`)**: Devir verilerini sözlük elemanı olarak verir. (bkz. **Devir -> d()**)
- **b_liste()**: Bilen verilerini (kişi başı ikramiye vs.) sözlük listesi olarak verir.  (bkz. **Bilen-> d()**)

### `TopSonuc` 
Diğer çekilişlerin sonuçları ve bilgileri.
- **tur** *(mpiyango.cekilis_turleri.x)*  bkz. **Çekiliş Türleri**
- **tur_str** *(str)*: Çekiliş türü ismi
- **hafta** *(int)*: Çekiliş hafta numarası
- **tarih** *(Tarih)*: Çekiliş tarihi
- **rakamlar** *(list[`int`])*: Kazanan rakamlar
- **sonuc** *(list[`int`])*: bkz. **rakamlar**
- **devir** *(`Devir`)*: Devretme verileri
- **hasilat** *(float)*: Elde edilen son hasılat
- **ikramiye** *(float)*: Devirlerle birlikte o haftanın ikramiyesi
- **bilenler** *(list[`Bilen`])*: Listede numaraları bilenlerin istatistikleri
- **il_ilce** *(`IlIlce`)*: Bilen il ve ilçeler
- **devird(`numara(int/str)`)**: Devir verilerini sözlük elemanı olarak verir. (bkz. **Devir -> d()**)
- **b_liste()**: Bilen verilerini (kişi başı ikramiye vs.) sözlük listesi olarak verir.  (bkz. **Bilen-> d()**)

## Fonksiyonlar

### mpiyango.tarihler(`mpiyango.cekilis_turleri.x`)

 - Verilen türdeki çekilişin www.mpi.gov.tr sitesinde sonuçları olan tarihlerini "Tarih" sınıfı içerisinde verir.
 
### mpiyango.sonuclar(`mpiyango.cekilis_turleri.x`, tarih(str/int/Tarih))

- Verilen türdeki oyunun verilen tarihteki sonucunu verir. Tarihler `Tarih` sınıfı ile verilmediyse `YYYYAAGG` formatında *str* ya da *int* olmalıdır.
Yazılacak.
