from animal import animal

class snake(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.habitat = habitat
        
    def info_snake(self):
        super().info_animal()
        print("jenis\t\t: ", self.jenis, "\nhabitat\t\t: ", self.habitat) # type: ignore
        
#objek
print()
snake = snake("ular kobra", "daging", "rindang", "bertelur", "berkulit sisik", "hutan")
print("== info snake ==")

snake.info_snake()

class snake(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.habitat = habitat
        
    def info_snake(self):
        super().info_animal()
        print("jenis\t\t: ", self.jenis, "\nhabitat\t\t: ", self.habitat) # type: ignore
        
#objek
print()
snake = snake("ular piton", "daging", "rawa", "bertelur", "berlian", "hutan")
print("== info snake ==")

snake.info_snake()

class snake(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.habitat = habitat
        
    def info_snake(self):
        super().info_animal()
        print("jenis\t\t: ", self.jenis, "\nhabitat\t\t: ", self.habitat) # type: ignore
        
#objek
print()
snake = snake("ular sawah", "hewan kecil", "sawah", "bertelur", "ditutupi sisik", "perairann")
print("== info snake ==")

snake.info_snake()