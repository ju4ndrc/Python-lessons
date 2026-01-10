class Products:
    def __init__(self,name,*args,**kwargs):
        self.name = name
        self.products = args
        self.discounts = kwargs

    def show_order(self):
        return f'{self.name} - {self.products} - {self.discounts}'   
    def show_total(self):

        total = sum(self.products)

        for key,value in self.discounts.items():
            return (total-(total*(value/100)))

         

karol = Products('Karol',10000,5000,500000,discount=5)

result = karol.show_order()

disc = karol.show_total()
print(result)
print(disc)
