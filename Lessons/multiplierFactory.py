class MultiplierFactory:
    
   #este metodo crea una nueva instancia y se controla la creacion de cada uno de los objetos
    def __new__(cls, factor: int):
        print(f"Creando instancia con factor {factor}")
        return super(MultiplierFactory, cls).__new__(cls)#Se establece como super esta miraa clase 
    
    def __init__(self, factor: int):
        print(f"Inicializando con factor {factor}")
        self.factor = factor
    
    def __call__(self, number: int) -> int:
        return number * self.factor
    
multiplier = MultiplierFactory(5)

result = multiplier(10)
print(result) 