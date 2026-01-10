class Circle:
    def __init__(self,radius:float)->None:
        self._radius = radius


    @property
    def area(self)->float:
        return  3.1416 * (self._radius**2) 

    @property
    def radius(self)->float:
        return self._radius

    @radius.setter
    def radius(self,value:float):
        if value < 0:
            raise ValueError('El radio no puede ser negativo')
        self._radius = value

new = Circle(10)


new.radius 

print(new.radius)
