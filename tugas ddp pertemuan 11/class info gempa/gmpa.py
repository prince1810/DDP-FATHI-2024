class gempa:
    # komstruktor Inisialisasi atribut dan skala
    def __init__(self, lokasi, skala):
        
        #atribut 
        self.lokasi = lokasi
        self.skala = skala
        
    # method menentukan dampak skala gempa
    def dampak(self):
      
        #statement / logika
        if self.skala < 5:
            print('Gempa kecil, tidak ada dampak')
        elif self.skala < 7:
            print('Gempa sedang, ada kerusakan ringan')
        elif self.skala < 8:
            print('Gempa kuat, ada kerusakan berat')
        elif self.skala < 10:
            print('Gempa sangat kuat, ada kerusakan parah')
            
        # menanmpilkan loksi dan skala
        print(f'lokasi gempa: {self.lokasi}')
        print(f'skala gempa: {self.skala}')