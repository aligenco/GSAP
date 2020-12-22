"""
KULLANICIDAN 0-100 ARASI BİR SAYI TUTMASI İSTENİYOR. PROGRAM BU SAYIYI BULMAYA ÇALIŞIYOR.
PROGRAMIN TAHMİN ETTİĞİ SAYI BÜYÜK İSE "B" KÜÇÜK İSE "K" DOĞRU İSE "D" KARAKTERLERİNİN GİRİLMESİ İSTENİYOR.
HATA GİRİŞ OLUR İSE TEKRAR SORULMAKTADIR. "D" DEĞERİ ALINDIĞINDA DA EKRANA TAHMİN SAYISI VE HATA SAYISI YAZILMAKTADIR.
"""
minn = 0 #iLK DEĞERLERİN VERİLMESİ
maxx = 100 #İLK DEĞERLERİN VERİLMESİ
tahmin = 0 #İLK DEĞERLERİN VERİLMESİ
hata = 0 #İLK DEĞERLERİN VERİLMESİ
while True: #SONSUZ DÖNDÜ OLUŞTURULDU VE SADECE "break" KOMUTU İLE DÖNGÜ SONLANDIRILACAK
    sayi = int(((maxx - minn)/2) + minn) #TAHMİN SAYİSİNİN ORTA SAYI ALINARAK OLUŞTURULMASI
    print("Tutulan sayi:", sayi) #TAHMİN EDİLEN SAYININ EKRANA YAZILMASI
    sonuc = input("Sayi (D)oğru mu, (B)üyük mü, (K)üçük mü?:") #TUTULAN SAYININ SORULMASI. TAHMİN BÜYÜK İSE B, KÜÇÜK İSE K GİRİLMELİDİR.
    tahmin = tahmin+1
    if sonuc == "D": # SAYI DOĞRU İSE BU KISIM ÇALIŞTIRILIYOR
        print("\nSonuç:", sayi)
        print("Tahmin sayisi:", tahmin-hata)
        print("Hatali giris sayisi:", hata)
        break #SAYI DOĞRU OLDUĞUNDAN WHİLE DÖNGÜSÜNDEN ÇIKILIYOR.
    elif sonuc == "B": # TAHMİN EDİLEN SAYI BÜYÜK İSE BU KISIM ÇALIŞTIRILIYOR
        maxx = sayi # TAHMNİN EDİKEN SAYI BÜYÜK OLDUĞUNDAN MAXX DEĞERE BU SAYI ATILIYOR VE YENİ DÖNGÜYE GEÇİLİYOR
    elif sonuc == "K": # TAHMİN EDİLEN SAYI KÜÇÜK İSE BU KISIM ÇALIŞTIRILIYOR
        minn = sayi # TAHMİN EDİLEN SAYI KÜÇÜK OLDUĞUNDAN MİNN SAYISINA BU SAYI ATILIYOR VE YENİ DÖNGÜYE GEÇİLİYOR.
    else:
        print("Hatalı değer girdiniz. Tekrar deneyiniz.")
        hata = hata+1