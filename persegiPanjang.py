class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def __str__(self):
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

if panjang == 0 or lebar == 0:
    print("Panjang dan lebar harus lebih besar dari 0")
else:
    pp = PersegiPanjang(panjang, lebar)
    print(pp)
    print(f"Luas Persegi Panjang: {pp.luas()}")
    print(f"Keliling Persegi Panjang: {pp.keliling()}")
    print(pp.__str__())