class Heigth:
    def __init__(self, name , heigh):
        self.name = name
        self.heigh = heigh

    def know_heigt(self):
        result = (self.heigh * 1.62)
        return f'Hola {self.name} tu peso en la luna es:{result}'
    

name = input("Introduce tu nombre\n")

heig = float(input("Introduce tu peso en kilos\n"))

user = Heigth(name,heig)

moon = user.know_heigt()

print(moon)