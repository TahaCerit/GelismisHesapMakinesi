Ekran = "GELİŞMİŞ HESAP MAKİNESİ"
print("*"*len(Ekran), Ekran, "*"*len(Ekran), sep="\n")

import math
from math import *
import time
from math import *
print("\n""""İŞLEMLER

********
1-Toplama                                           (topla)
2-Çıkarma                                           (çıkar)
3-Çarpma                                            (çarp)
4-Bölme                                             (böl)
5-Faktöriyel Bulma                                  (faktöriyel)
6-Karekökünü Bulma                                  (karekök)
7-İki Sayının Logaritmasını Bulma  örnek:(25,5)     (log) 
8-Hipotenüsünü Bulma                                (pisagor)

Çıkış                                               (q)
""")
while True:
    işlem = input("Lütfen İşlemin Kısaltımını Giriniz:")
    if işlem == ("topla"):
        print("Toplama İşlemi Seçildi..")
        time.sleep(1)
        toplama1=int(input("İlk Sayıyı Giriniz:"))
        toplama2=int(input("İlk Sayıyı Giriniz:"))
        print("{} sayısı ile {} sayısının toplamı {} dır.".format(toplama1,toplama2,toplama1+toplama2))
    elif işlem == ("çıkar"):
        print("Çıkarma İşlemi Seçildi..")
        time.sleep(1)
        çıkarma1=int(input("İlk Sayıyı Giriniz:"))
        çıkarma2=int(input("İlk Sayıyı Giriniz:"))
        print("{} sayısı ile {} sayısının farkı {} dır.".format(çıkarma1,çıkarma2,çıkarma1-çıkarma2))
    elif işlem == ("çarp"):
        print("Çarpma İşlemi Seçildi..")
        time.sleep(1)
        çarpma1=int(input("İlk Sayıyı Giriniz:"))
        çarpma2=int(input("İlk Sayıyı Giriniz:"))
        print("{} sayısı ile {} sayısının çarpımı {} dır.".format(çarpma1,çarpma2,çarpma1*çarpma2))
    elif işlem == ("böl"):
        print("Bölme İşlemi Seçildi..")
        time.sleep(1)
        bölme1=int(input("İlk Sayıyı Giriniz:"))
        bölme2=int(input("İlk Sayıyı Giriniz:"))
        print("{} sayısının {} sayısına bölümü {} dır.".format(bölme1,bölme2,bölme1/bölme2))
    elif işlem ==("faktöriyel"):
        print("Faktöriyel Bulma İşlemi Seçildi..")
        time.sleep(1)
        faktöriyel=int(input("Faktöriyelini Alacağınız Sayıyı Giriniz:"))
        factorial(faktöriyel)
        print("{} sayısının faktöriyeli {} sayısıdır.".format(faktöriyel,factorial(faktöriyel)))
    elif işlem == ("karekök"):
        print("Karekökünü Bulma İşlemi Seçildi..")
        time.sleep(1)
        karekök=int(input("Karekökünü Alacağınız Sayıyı Giriniz:"))
        sqrt(karekök)
        print("{} sayısının karekökü {} sayısıdır.".format(karekök,sqrt(karekök)))
    elif işlem == ("log"):
        print("İki Sayının Logaritmasını Bulma İşlemi Seçildi..")
        time.sleep(1)
        logaritma1=int(input("Birinci Değeri Giriniz:"))
        logaritma2=int(input("İkinci Değeri Giriniz:"))
        log(logaritma1,logaritma2)
        print("Birinci değerin ikinci değere göre logaritması ({},{}) = {} dır.".format(logaritma1,logaritma2,log(logaritma1,logaritma2)))
    elif işlem == ("pisagor"):
        print("Hipotenüsünü Bulma İşlemi Seçildi..")
        time.sleep(1)
        pisagor1=int(input("İlk Değeri Giriniz:"))
        pisagor2=int(input("İkinci Değeri Giriniz:"))
        hypot(pisagor1,pisagor2)
        print("İlk değeri {} ,İkinci değeri {} olan iki sayının Hipotenüsü {} dir".format(pisagor1,pisagor2,hypot(pisagor1,pisagor2)))
    else:
        işlem == "q"
        print("Programdan Sonlandırılıyor...")
        time.sleep(2)
        print("Programdan Sonlandırıldı...")
        break
