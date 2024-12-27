class animal:
    # konstruktor properti
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    # method informasi
    def info_animal(self):
        print("nama hewan\t: ", self.nama, "\nmakanan\t\t: ", self.makanan, "\nhidup\t\t: ", self.hidup, "\nberkembang_biak\t: ", self.berkembang_biak)
    
# # objek
# kucing = animal("kucing", "daging", "daratan", "melahirkan")

# kucing.info_animal()