# Parent class
class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info(self):
        return f"Nama: {self.name}, Makanan: {self.makanan}, Hidup: {self.hidup}, Berkembang Biak: {self.berkembang_biak}"

# Child class: Burung
class Burung(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna

    def terbang(self):
        return f"{self.name} sedang terbang."

# Child class: Ikan
class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, habitat, jenis):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.jenis = jenis

    def berenang(self):
        return f"{self.name} sedang berenang di {self.habitat}."

# Child class: Ular
class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, panjang, warna):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.panjang = panjang
        self.warna = warna

    def melata(self):
        return f"{self.name} sedang melata."

# Membuat objek dari masing-masing class child
burung1 = Burung("Elang", "Daging", "Udara", "Bertelur", "Raptor", "Coklat")
burung2 = Burung("Merpati", "Biji-bijian", "Udara", "Bertelur", "Kolumbidae", "Abu-abu")
burung3 = Burung("Kakatua", "Buah-buahan", "Udara", "Bertelur", "Psittacidae", "Putih")

ikan1 = Ikan("Ikan Mas", "Pelet", "Air Tawar", "Bertelur", "Kolam", "Cyprinidae")
ikan2 = Ikan("Ikan Salmon", "Serangga", "Air Laut", "Bertelur", "Sungai", "Salmonidae")
ikan3 = Ikan("Ikan Betta", "Pelet", "Air Tawar", "Bertelur", "Akuarium", "Osphronemidae")

ular1 = Ular("Ular Piton", "Mamalia", "Daratan", "Bertelur", "5 meter", "Hijau")
ular2 = Ular("Ular Kobra", "Mamalia", "Daratan", "Bertelur", "3 meter", "Coklat")
ular3 = Ular("Ular Boa", "Mamalia", "Daratan", "Bertelur", "4 meter", "Bercorak")

# Menampilkan informasi dan metode dari objek
print(burung1.info())
print(burung1.terbang())

print(ikan1.info())
print(ikan1.berenang())

print(ular1.info())
print(ular1.melata())