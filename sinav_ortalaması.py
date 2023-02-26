sinavnotu1 = int(input("1. sinav notunuzu giriniz: "))
sinavnotu2 = int(input("2. sinav notunuzu giriniz: "))

ortalama=(sinavnotu1+sinavnotu2)/2

print("Sinif ortalamaniz: {0} ".format(ortalama))

if(ortalama >= 50):
    print("Bravo sinifi gectiniz.")
else:
    print("Maalesef sinifta kaldiniz. Bir daha ki sene gorusmek uzere")
if(70 > ortalama >= 50):
    print("Bu sene maalesef bir basari belgesi alamadiniz.")
if(85 > ortalama >= 70):
    print("Tebrikler bu sene Tesekkur Belgesi aldiniz.")
if(100 >= ortalama >= 85):
    print("Tebrikler bu seneyi Takdir Belgesi ile tamamladiniz.")