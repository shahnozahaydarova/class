class GulObod:
    def __init__(self,tur,narx):
        self.tur = tur
        self.narx = narx
    def chiqarish(self):
        print("Mahsulot turi: ",self.tur,"Mahsulot o'rtacha  narxi: ", self.narx)

m1 = GulObod("Naushnik",3000000)
m2 = GulObod("Kompyuter",6000000)
m3 = GulObod("Telefon",5000000)
print(m1.chiqarish())
print(m2.chiqarish())
print(m3.chiqarish())

 
tanlov = input('''Sizga qaysi turdagi mahsulot kerak:
1 == Naushnik
2 == kompyuter
3 == telefon                    
''')

class Naushnik(GulObod):
    def __init__(self, tur, narx, rang):
        super().__init__(tur, narx)
        self.rang = rang
    def chiqarish1(self):
        print("Siz tanlagan mahsulot Naushnik: Turi:",self.tur,"Narxi: ", self.narx,"Rangi: ",self.rang)

t1 = Naushnik("Oddiy ",40000,"qora")
t2 = Naushnik("Bluetoth ", 200000,"jigarrang")
t3 = Naushnik("Simsiz ",150000,"oq")

class Kompyuter(GulObod):
    def __init__(self,tur,narx,olchami):
        super().__init__(tur,narx)
        self.olchami = olchami
    def chiqarish2(self):
        print("Siz tanlagan mahsulot Kompyuter : Turi:",self.tur,"Narxi: ", self.narx,"O'lchami : ",self.olchami)

k1 = Kompyuter("acer",8000000,"80*50")
k2 = Kompyuter("hp",9000000,"80*50")
k3 = Kompyuter("lenovo",7000000,"70*50")


class Telefon(GulObod):
    def __init__(self,tur,narx,xotira):
        super().__init__(tur,narx)
        self.xotira = xotira
    def chiqarish3(self):
        print("Siz tanlagan mahsulot Telefon: Turi:",self.tur,"Narxi: ", self.narx,"Xotirasi : ",self.xotira)

tt1 = Telefon("Redmi",7000000,"64")
tt2 = Telefon("Samsung",800000,"16")
tt3 = Telefon("Iphone",10000000,"128")


if tanlov == '1':
    print(t1.chiqarish1())
    print(t2.chiqarish1())
    print(t3.chiqarish1())
elif tanlov =='2':
    print(k1.chiqarish2())
    print(k2.chiqarish2())
    print(k3.chiqarish2())
elif tanlov =='3':
    print(tt1.chiqarish3())
    print(tt2.chiqarish3())
    print(tt3.chiqarish3())
else:
    print("Siz tanlagan mahsulot bizda mavjud emas.")