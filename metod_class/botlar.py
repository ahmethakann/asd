class Personal:
    
    personel_sayisi =0
    zam_orani = 1.05

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = f'{ad}.{soyad}@smartmaple.com'
        
        Personal.personel_sayisi += 1

    def tam_ad(self): #sıradan metod
        return f"{self.ad.title()} {self.soyad.title()}"

    def zam_uygula(self): #sıradan metod
        self.maas = int(self.maas * self.zam_orani)

    @classmethod #class metod decoratoru
    def zam_oraninini_belirle(cls, oran): #bu class metod sayesinde sadece per1 in maaşına zam yapsak bile sınıftaki herkesin zam oranını değiştirmiş olacağız.
        eski_oran = cls.zam_orani
        cls.zam_orani = oran
        print(f"Zam oranı {eski_oran} den {cls.zam_orani} e yükseltilmiştir.")

    @classmethod #class metod decoratoru
    def from_string(cls, per_str): #bu class metod sayes
        ad, soyad, maas = per_str.split("-")
        return cls(ad, soyad, maas)

    @staticmethod #static metod decoratoru
    def is_workday(gun): #static metodlar sınıfın özelliklerini kullanmazlar.
        if gun.weekday() == 5 or gun.weekday() == 6:
            return "Hafta sonu"
        else:
            return "Hafta içi"

#personel bilgileri ve personel saysı 
print(Personal.personel_sayisi)
per1 = Personal("ali", "çakır", 10000)
print(Personal.personel_sayisi)
per2 = Personal("ayşe", "sevgi", 12000)
print(Personal.personel_sayisi)

print(per1.maas)
Personal.zam_uygula(per1)
print(per1.maas)

print(Personal.tam_ad(per2))

Personal.zam_oraninini_belirle(1.1)
print(Personal.zam_orani)
print(per1.zam_orani)
print(per2.zam_orani)

yeni_per_str_1 = Personal.from_string("ahmet-çakır-15000")
per_str_2 = "mehmet-bilgiç-12000"
print(yeni_per_str_1.eposta)

from datetime import date

tarih = date(2023, 1, 15)
print(tarih.day)
print(Personal.is_workday(tarih))