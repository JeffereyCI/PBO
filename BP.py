class Prima:
    def __init__(self, angka : int):
        self.angka = angka
        self.status = ""

    def validasiPrima(self):
        if self.angka < 2:
            self.status = False
            return
        for i in range(2, self.angka):
            if self.angka % i == 0:
                self.status = False
                return self.status
        
        self.status = True
        
    def cetakHasil(self):
        if self.status is True:
            print("Bilangan Prima")
        else:
            print("Bukan Bilangan Prima")

def main():
    coba1 = Prima(81)
    coba1.validasiPrima()
    coba1.cetakHasil()

if __name__ == "__main__":
    main()