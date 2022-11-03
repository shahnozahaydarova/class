class MaishiyTexnika:
    def __init__(self,tur,narx):
        self.tur = tur
        self.narx = narx
    def chiqarish(self):
        print("Bizda quyidagi mahsulotlar mavjud: ",self.tur,"O'rtacha narxi: ",self.narx)

m1 = MaishiyTexnika("1. Televizorlar",3000333)
m2 = MaishiyTexnika("2. Gaz plitalar",2000000)
m3 = MaishiyTexnika("3. Muzlatgichlar",5000000)

print(m1.chiqarish())
print(m2.chiqarish())
print(m3.chiqarish())



tanlov = input("Qaysi mahsulotimiz haqida aniqroq malumotga ega bo'lishni xoxlaysiz:     ")



class Televizor(MaishiyTexnika):
    def __init__(self,tur,narx,rang,nom):
        super().__init__(tur,narx)
        self.rang = rang
        self.nom = nom
    def chiqarish1(self):
        print("Bizda quyidagi televizorlar mavjud.Turi: ",self.tur,",Narxi: ",self.narx,",Rangi: ",self.rang,",Nomi:",self.nom)

t1 = Televizor("Ultra HD",'40000',"qora","Artel")
t2 = Televizor("Led",'500000',"qora","Samsung")
t3 = Televizor("3d",'450000',"qora","Vesta")


class GazPlita(MaishiyTexnika):
    def __init__(self,tur,narx,rang):
        super().__init__(tur,narx)
        self.rang = rang
    def chiqarish2(self):
        print("Bizda quyidagi gaz plita mavjud.Turi: ",self.tur,",Narxi: ",self.narx,",Rangi: ",self.rang)

g1 = GazPlita("Artel",3000000,"oq")
g2 = GazPlita("Ideal",2500000,"kulrang")
g3 = GazPlita("GoodWell",4000000,"qora")


class Muzlatgich(MaishiyTexnika):
    def __init__(self,tur,narx,uzunlik):
        super().__init__(tur,narx)
        self.uzunlik = uzunlik
    def chiqarish3(self):
        print("Bizda quyidagi turdagi muzlatgich mavjud.Turi: ",self.tur,",Narxi: ",self.narx,",Uzunligi: ",self.uzunlik)


mm1 = Muzlatgich("Shivaki",15000000,"2m")
mm2 = Muzlatgich("Artel",6000000,"1.5m")
mm3 = Muzlatgich("Premier",4000000,"1.5m")



if tanlov == '1':
    print(t1.chiqarish1())
    print(t2.chiqarish1())
    print(t3.chiqarish1())
elif tanlov == '2':
    print(g1.chiqarish2())
    print(g2.chiqarish2())
    print(g3.chiqarish2())
elif tanlov == '3':
    print(mm1.chiqarish3())
    print(mm2.chiqarish3())
    print(mm3.chiqarish3())
