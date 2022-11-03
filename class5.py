class Odam:
    def __init__(self,ism,familiya):
        self.ism = ism
        self.familiya = familiya
    def chiqarish(self):
        print("Ismi: ",self.ism,"Familiyasi: ",self.familiya)

o1 = Odam("Shukrona","Nurova")
o2 = Odam("Mustafo","Ibragimov")
o3 = Odam("Maryam","Nasriddinova")
print(o1.chiqarish())
print(o2.chiqarish())
print(o3.chiqarish())

class Dasturchi(Odam):
    def __init__(self, ism, familiya,yunalish):
        super().__init__(ism,familiya)
        self.yunalish = yunalish
    def chiqarish1(self):
        print("Dasturchi ismi:",self.ism,"Familiyasi: ",self.familiya,"Yo'nalishi: ",self.yunalish)
d1 = Dasturchi("Shukrona","Nurova",'python')
d2 = Dasturchi("Muhammadjon","ILhomov",'frontend')
d3 = Dasturchi("Guli",'Erkinova',"backend")
print(d1.chiqarish1())
print(d2.chiqarish1())
print(d3.chiqarish1())

class Oqituvchi(Odam):
    def __init__(self, ism, familiya,fan):
        super().__init__(ism,familiya)
        self.fan = fan
    def chiqarish1(self):
        print("O'qituvchi ismi:",self.ism,"Familiyasi: ",self.familiya,"Ta'lim beradigan fani: ",self.fan)
oo1 = Oqituvchi("Shukrona","Tosheva",'informatika')
oo2 = Oqituvchi("Sardor","Hojiyev",'matematika')
oo3 = Oqituvchi("Sevinch",'Yodgorova',"tabiat")
print(oo1.chiqarish1())
print(oo2.chiqarish1())
print(oo3.chiqarish1())

class Nafaqahor(Odam):
    def __init__(self, ism, familiya,nafaqa_puli):
        super().__init__(ism,familiya)
        self.nafaqa_puli = nafaqa_puli
    def chiqarish2(self):
        print("Nafaqaho'r ismi:",self.ism,"Familiyasi: ",self.familiya,"Nafaqa puli: ",self.nafaqa_puli)
n1 = Nafaqahor("Shukrona","Nurova",2000000)
n2 = Nafaqahor("Muhammadali","Ramazonov",1500000)
n3 = Nafaqahor("Muharram",'Sultonova',2000000)
print(n1.chiqarish2())
print(n2.chiqarish2())
print(n3.chiqarish2())
        