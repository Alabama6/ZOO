
class Animal(object):

    def __init__(self):
        self.wiek = 0
        self.waga = 0
        self.wzrost = 0
        self.gatunek = ''

    def get_wiek(self):
        return self.wiek

    def get_waga(self):
        return self.waga

    def get_wzrost(self):
        return self.wzrost

    def get_gatunek(self):
        return self.gatunek

    def set_wiek(self):
        return self.wiek

    def set_waga(self):
        return self.waga

    def set_wzrost(self):
        return self.wzrost

    def set_gatunek(self):
        return self.wzrost



animal = Animal()

animal.waga = 2
animal.set_waga(2)

print animal.waga
print animal.get_waga() #zabezpieczenie kodu
