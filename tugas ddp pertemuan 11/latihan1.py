class orang:
    # properti
    nama = "fathi" # type: ignore
    umur = 0 # type: ignore
    jekel = "" # type: ignore
    
    # method
    def ngomong(self, kata):
        print("saya bisa bicara")
    
    def jalan(selft):
        print("saya bisa berjalan, kapan ??")
        
        
# objek1
supir = orang()
print(supir.nama)
supir.ngomong("karena saya perempuan")
supir.sim = "A"
print("saya punya SIM", supir.sim)