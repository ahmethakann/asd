from rest_framework import serializers
from haberler.models import Makale, Gazeteci

from datetime import datetime
from datetime import date
from django.utils.timesince import timesince




# MODEL SERIALIZER
class MakaleSerializer(serializers.ModelSerializer):
    
    time_since_pub = serializers.SerializerMethodField()
    # yazar = serializers.StringRelatedField()
    # yazar = GazeteciSerializer()

    class Meta:
        model = Makale
        fields = '__all__'
        # fields = ['time_since_pub','baslik']
        read_only_fields = ['id', 'yaratilma_tarihi', 'guncellenme_tarihi']

    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.yayimlanma_tarihi
        pub_date = datetime.date(pub_date)
        if object.aktif == True:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return "Aktif Değil !"    


    def validate_yayımlanma_tarihi(self, tarih_degeri):
        today = date.today()
        if tarih_degeri > today:
            raise serializers.ValidationError("Yayımlanma tarihi bugünden sonra olamaz")
        return tarih_degeri


class GazeteciSerializer(serializers.ModelSerializer):
    
    # makaleler = MakaleSerializer(many=True, read_only=True)
    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay',
    )


    class Meta:
        model = Gazeteci
        fields = '__all__'




# STANDART SERIALIZER
# class MakaleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     yazar = serializers.CharField()
#     baslik = serializers.CharField()
#     aciklama = serializers.CharField()
#     metin = serializers.CharField()
#     sehir = serializers.CharField()
#     yayimlanma_tarihi = serializers.DateTimeField()
#     aktif = serializers.BooleanField()
#     yaratilma_tarihi = serializers.DateTimeField(read_only=True)
#     guncellenme_tarihi = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return Makale.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.yazar = validated_data.get('yazar', instance.yazar)
#         instance.baslik = validated_data.get('baslik', instance.baslik)
#         instance.aciklama = validated_data.get('aciklama', instance.aciklama)
#         instance.metin = validated_data.get('metin', instance.metin)
#         instance.sehir = validated_data.get('sehir', instance.sehir)
#         instance.yayimlanma_tarihi = validated_data.get('yayimlanma_tarihi', instance.yayimlanma_tarihi)
#         instance.aktif = validated_data.get('aktif', instance.aktif)
#         instance.save()
#         return instance

#     def validate(self, data): # OBJECT LEVEL VALIDATION
#         if data['baslik'] == data['aciklama']:
#             raise serializers.ValidationError("Aciklama ve başlık aynı olamaz!")
#         return data

#     def validate_baslik(self, value):# TEK ALAN (FIELD) LEVEL VALIDATION
#         if len(value) < 20:
#             raise serializers.ValidationError(f"Başlık 20 karakterden az olamaz! Siz {len(value)}  karakter girdiniz.")
#         return value
