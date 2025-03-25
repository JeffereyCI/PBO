class Bintang:
    def __init__(self, angka : int):
        self.angka = angka

    def cetakBintang(self) -> None:
        for i in range(self.angka, 0, -1):
            print("*" * i, end="\n")
            # print("\n")

def main():
    coba1 = Bintang(3)
    coba1.cetakBintang()

if __name__ == "__main__":
    main()