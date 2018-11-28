from animal import Animal


class Bird(Animal):

    def __init__(self):
        super(Animal, self).__init__() #moge zainicjalizowac klase nie dziedziczac jej , poza jakakolwiek klasa np w jakiejs funkcji che wywol;ac sobie np klase animal-> super
        #lub:
        Animal.__init__(self)
        self.dlugosc_skrzydla = 0
        self.kolor_upierzenia = ''
        self.plec = ''

    def get_dlugosc_skrzydla(self):
        return self.dlugosc_skrzydla

    def get_kolor_upierzenia(self):
        return self.kolor_upierzenia

    def get_plec(self):
        return self.plec

    def set_dlugosc_skrzydla(self):
        return self.dlugosc_skrzydla

    def set_kolor_upierzenia(self):
        return self.kolor_upierzenia

    def set_plec(self):
        return self.plec

bird  = Bird()
bird.get_waga()


#git diff przed git add  - sprawdzam roznice


