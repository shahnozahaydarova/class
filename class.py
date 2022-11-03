class Ichimlik:
    def __init__(self,tur,hajm,narx):
        self.tur = tur
        self.hajm = hajm
        self.narx = narx
    def __str__(self):
        return f"Turi: {self.tur}, Hajmi: {self.hajm},Narxi: {self.narx}"
i1 = Ichimlik("Pepsi","1.5l","12000")
i2 = Ichimlik("Coca cola","0.5l","5000")
i3 = Ichimlik("Sprite","1l","10000")
print(i1)
print(i2)
print(i3)


class Shahar:
    def __init__(self,nom,poytaxt,maydon):
        self.nom = nom
        self.poytaxt = poytaxt
        self.maydon = maydon
    def __str__(self):
        return f"Davlat nomi: {self.nom},Poytaxti: {self.poytaxt},Maydoni:{self.maydon}"
d1 = Shahar("Toshkent","O'zbekiston","449000")
d2 = Shahar("Italiya","Rim","123450")
d3 =Shahar("Germaniya","Berlin","549120")
print(d1)
print(d2)
print(d3)


class Poyabzal:
    def __init__(self,tur,razmer,narx):
        self.tur = tur
        self.razmer = razmer
        self.narx = narx
    def __str__(self):
        return f"Turi: {self.tur},Razmeri: {self.razmer},Narxi:{self.narx}"
p1 = Poyabzal("Krasofka","40","300000")
p2 = Poyabzal("Tufli","38","250000")
p3 =Poyabzal("Etik","39","350")
print(p1)
print(p2)
print(p3)



class Kompyuter:
    def __init__(self,nom,rang,protsessor):
        self.nom = nom
        self.rang = rang
        self.protsessor = protsessor
    def __str__(self):
        return f"nomi: {self.nom},rang: {self.rang},protsessor:{self.protsessor}"
p1 = Shahar("acer","oq","intel")
p2 = Shahar("hp","oq","AMD")
p3 =Shahar("fpb","qora","celeron")
print(p1)
print(p2)
print(p3)


class Odam:
    def __init__(self,ism,familiya,yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
    def __str__(self):
        return f"ism: {self.ism},familiya: {self.familiya},yosh:{self.yosh}"
o1 = Odam("Shahlo","Tosheva","10")
o2 = Odam("Laylo","Tosheva","50")
o3 =Odam("Iroda","Tosheva","5")
print(o1)
print(o2)
print(o3)