class Kitob:
    def __init__(self,tur,muqova):
        self.tur = tur
        self.muqova = muqova

    def chiqarish(self):
        print("Tanlangan kitobingiz turi: ",self.tur,"Muqovasi: ",self.muqova)

k1 = Kitob("Badiiy","qattiq")
k2 = Kitob("Darslik","yumshoq")
print(k1.chiqarish())
print(k2.chiqarish())
a = input('''Qaysi turdagi qanday kitobni olishni xoxlaysiz:
1 == Badiiy
2 ==  Darslik

''')
class Badiiy(Kitob):
    def __init__(self,tur,muqova,narxi,asar_muallifi):
        super().__init__(tur,muqova)
        self.narxi = narxi
        self.asar_muallifi = asar_muallifi
    def chiqarish1(self):
        print("Asar nomi:",self.tur,"Muqovasi:",self.muqova,"Narxi: ",self.narxi,"Asar muallifi: ",self.asar_muallifi)

b1 = Badiiy("Odam bo'lish qiyin","yumshoq","40000","O'lmas Umarbekov")
b2 = Badiiy("O'tkan kunlar","qattiq","50000","o'tkir Hoshimov")
b3 = Badiiy("Olim yetishtirgan onalar","qattiq",60000,"Murod To'sun")

class Darslik(Kitob):
    def __init__(self,tur,muqova,sinf):
        super().__init__(tur,muqova)
        self.sinf = sinf
    def chiqarish2(self):
        print("Darslik nomi: ",self.tur,"Muqovasi: ",self.muqova,"Sinfi:",self.sinf)
d1 = Darslik("Informatika","yumshoq",8)
d2 = Darslik("Matematika","yumshoq",11)
d3 = Darslik("Fizika","yumshoq",7)        

if a == '1': 
    print("Siz badiiy kitoblar haqida  ma'lumotga ega bo'lishingiz mumkin.")
    print(b1.chiqarish1())
    print(b2.chiqarish1())
    print(b3.chiqarish1())
elif a == '2':
    print("Siz darslik kitoblar haqida  ma'lumotga ega bo'lishingiz mumkin.")
    print(d1.chiqarish2())
    print(d2.chiqarish2())
    print(d3.chiqarish2())