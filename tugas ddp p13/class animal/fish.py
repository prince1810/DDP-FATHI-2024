from animal import animal

class fish(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernafas, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernafas = bernafas
        self.habitat = habitat
        
    def info_fish(self):
        super().info_animal()
        print("bernafas\t: ", self.bernafas, "\nhabitat\t\t: ", self.habitat) # type: ignore
        
#objek
print()
fish = fish("lumba-lumba", "ikankecil", "lautan", "vivipar", "paru-paru", "air asin dan tawar")
print("== info fish ==")

fish.info_fish()

class fish(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernafas, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernafas = bernafas
        self.habitat = habitat
        
    def info_fish(self):
        super().info_animal()
        print("bernafas\t: ", self.bernafas, "\nhabitat\t\t: ", self.habitat) # type: ignore
        
#objek
print()
fish = fish("Hiu", "daging", "samudra", "ovivipar", "insang", "air asin")
print("== info fish ==")

fish.info_fish()

class fish(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernafas, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernafas = bernafas
        self.habitat = habitat
        
    def info_fish(self):
        super().info_animal()
        print("bernafas\t: ", self.bernafas, "\nhabitat\t\t: ", self.habitat) # type: ignore
        
#objek
print()
fish = fish("paus", "plankton", "samudra", "vivipar", "paru-paru", "air asin")
print("== info fish ==")

fish.info_fish()