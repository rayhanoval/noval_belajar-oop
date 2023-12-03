class Mamalia:
    lahiran = "heeenggg"
    def melahirkan(self, suara_lahir_new = ""):
        self.lahiran = suara_lahir_new or self.lahiran
        print(self.lahiran)

    def menyusui(self):
        print("susu susu")
    
class Monyet(Mamalia):
    def bersuara(self):
        print("uuu aaa")
    
    def berayun(self):
        print("yun ayun")

class Kambing(Mamalia):
    suaraKambing = "mbeee....."
    def mbee(self, kambing_suara_baru = ""):
        self.suaraKambing = kambing_suara_baru or self.suaraKambing
        print(self.suaraKambing)

    def kurban(self):
        print("T_T")