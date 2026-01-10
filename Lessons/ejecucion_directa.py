

class Calculator:
    
    def add(self,n1,n2):
        return n1+n2
    def mult(self,n1,n2):
        return n1*n2
    def div(self,n1,n2):
        if n2 == 0:
            raise ValueError('Cero division error')
        return n1/n2
    def minus(self,n1,n2):
        return n1-n2
    


    
if __name__ == "__main__":
    print('Operaciones\n')

    res_1 = Calculator()
    result1 = res_1.add(5,8)
    print(f"Suma:{result1}")

    res2 = Calculator()
    result2 = res2.mult(100,100)
    print(result2)
