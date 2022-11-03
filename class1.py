class Mebel:
    def __init__(self,tur):
        self.tur = tur
       
    def chiqarish(self):
        print("Bizda quyidagi turdagi mebellar mavjud: ",self.tur)
m1 = Mebel("Oshxona,mehmonxona")


print(m1.chiqarish())


a = input('''Sizga qaysi turdagi mebel haqida ko'proq ma'lumot kerak:
1 == Oshxona
2 == Mehmonxona
''')
class Oshxona(Mebel):
    def __init__(self,tur,rang,narx,olcham):
        super().__init__(tur)
        self.rang = rang
        self.narx=narx
        self.olcham =olcham 
    def chiqarish1(self):
        print("Turi:",self.tur,",Rangi:",self.rang,",Narxi:",self.narx,",o'lchami: ",self.olcham)

o1 = Oshxona("oshxona","Sizga manzur bo'ladigan rangda",10000000,"4m")
o2 = Oshxona("oshxona","Sizga manzur bo'ladigan rangda",15000000,"7m")



class Mehmonxona(Mebel):
    def __init__(self,tur,rang,narx,uzunlik):
        super().__init__(tur)
        self.rang = rang 
        self.narx = narx
        self.uzunlik = uzunlik
    def chiqarish2(self):
        print("Turi: ",self.tur,"Rangi: ",self.rang,",Narxi: ",self.narx,",Uzunligi: ",self.uzunlik)
mm1 = Mehmonxona("Mehmonxona","Sizga manzur bo'ladigan rangda",20000000,'6m')
mm2 = Mehmonxona("Mehmonxona","Sizga manzur bo'ladigan rangda",25000000,"7m")

if a == '1':
    print("Siz mehmonxona mebellari haqida malumot olishingiz mumkin.")
    print(o1.chiqarish1())
    print(o2.chiqarish1())
elif a == '2':
    print("Siz mehmonxona mebellari haqida malumot olishingiz mumkin.")
    print(mm1.chiqarish2())
    print(mm2.chiqarish2())