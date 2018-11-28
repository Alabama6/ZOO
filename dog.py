from animal import Animal


class Dog(object):

    def __init__(self, name, rasa, masc):
        self.name = name
        self.rasa = rasa
        self.masc = masc

    def __str__(self):
        return "Pies o imieniu {} pochodzacy z rasy {} o masci {}".format(self.name, self.rasa, self.masc)


dog = Dog('Reksio', 'kundelek', 'czarny')
print dog
