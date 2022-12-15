class Molecule: #定义Molecule作为基类
    def __init__(self):
        self.elements = set()   #初始化空集
        self.weight = None  #初始化为None
    def show_weight(self):  #定义show-weight方法
        print(self.weight)  
    def show_elements(self):    #定义show-element方法
        print(self.elements)

class AminoAcid(Molecule) : #定义AminoAcid类继承Molecule
    def __init__(self):
        super().__init__()
        self.composition = {'C': 0, 'H': 0, 'O': 0, 'N': 0, 'S': 0} #初始化空字典
        self.WEIGHT = {'C': 12, 'H': 1, 'O': 16, 'N': 14, 'S': 32}  #给不同元素赋值作为分子量
    def calc_mw(self): #定义calc-mw方法
        sum = 0
        for key in self.WEIGHT:
            self.composition.get(key)
            sum += self.WEIGHT[key]*self.composition[key]
        return sum  #对比compostition和weight的key，将key相同的值相乘再累加，得到分子量计算方法
    def show_weight(self) :
        self.weight = self.calc_mw()
        return super().show_weight()
    def show_elements(self) :
        for key in self.composition:
            if self.composition[key] != 0 :
               self.elements.add(key)
        return super().show_elements()  #将composition中非0的key选择并加入elements的空集中，作为元素

#定义三种氨基酸，通过查找化学式得到其分子量，再根据以上初始化方法对应赋值
#半胱氨酸--c3h7no2s
class Cysteine(AminoAcid) :
    def __init__(self) :
        super().__init__()
        self.composition = {'C': 3, 'H': 7, 'O': 2, 'N': 1, 'S': 1}
    def show_composition(self) :
        print(self.composition)
#异亮氨酸--c6h12no2s
class Isoleucine(AminoAcid) :
    def __init__(self) :
        super().__init__()
        self.composition = {'C': 6, 'H': 13, 'O': 2, 'N': 1, 'S': 0}
    def show_composition(self) :
        print(self.composition)
#亮氨酸--c6h12no2s
class Leucine(AminoAcid) :
    def __init__(self) :
        super().__init__()
        self.composition = {'C': 6, 'H': 13, 'O': 2, 'N': 1, 'S': 0}
    def show_composition(self) :
        print(self.composition)
    def is_isoform(self, aminoAcid):
        if (self.composition == aminoAcid.composition):
            return True
        return False    #判断亮氨酸和异亮氨酸调用后的返回值，判断其是否为同分异构
#亮氨酸
leu = Leucine()
print("亮氨酸-C6H13NO2-分子量：")
leu.show_weight()
print("元素集合：")
leu.show_elements()
print("元素字典：")
leu.show_composition()
#半胱氨酸
cyc = Cysteine()
print("半胱氨酸-C3H7NO2S-分子量：")
leu.show_weight()
print("元素集合：")
leu.show_elements()
print("元素字典：")
leu.show_composition()
#异亮氨酸
iso = Isoleucine()
print("异亮氨酸-C6H13NO2-分子量：")
leu.show_weight()
print("元素集合：")
leu.show_elements()
print("元素字典：")
leu.show_composition()
#通过返回值计的得出布尔值
print(f"亮氨酸和异亮氨酸是否是同分异构体?\n{leu.is_isoform(iso)}")
print(f"亮氨酸和半胱氨酸是否是同分异构体?\n{leu.is_isoform(cyc)}")
#生成三种氨基酸的实例，并调用上述各种方法
