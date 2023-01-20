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

    @classmethod #class metod
    def zam_oraninini_belirle(cls, oran):
        cls.zam_orani = oran

print(Personal.personel_sayisi)
per1 = Personal("ali", "çakır", 10000)
print(Personal.personel_sayisi)
per2 = Personal("ayşe", "sevgi", 12000)
print(Personal.personel_sayisi)

print(per1.maas)
Personal.zam_uygula(per1)
print(per1.maas)

print(Personal.tam_ad(per2))