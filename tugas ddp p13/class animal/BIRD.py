from animal import animal

class bird(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh
        
    # method
    def info_bird(self):
        super().info_animal()
        print("warna\t\t: ", self.warna, "\nparuh\t\t: ", self.paruh) # type: ignore
    
bird = bird("burung hantu", "daging", "tepian sungai", "bertelur", "coklat tua", "bengkok")
print('## Info Bird ##')

bird.info_bird()

class bird(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh
        
    # method
    def info_bird(self):
        super().info_animal()
        print("warna\t\t: ", self.warna, "\nparuh\t\t: ", self.paruh) # type:
    
bird = bird("garuda", "daging", "tebing", "bertelur", "merah", "bengkok")
print('## Info Bird ##')

bird.info_bird()

class bird(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh
        
    # method
    def info_bird(self):
        super().info_animal()
        print("warna\t\t: ", self.warna, "\nparuh\t\t: ", self.paruh) # type:
    
bird = bird("elangjawa", "daging", "tebing", "bertelur", "coklat", "bengkok")
print('## Info Bird ##')

bird.info_bird()