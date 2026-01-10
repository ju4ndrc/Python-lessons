class Employee:
    def __init__(self,name,*args,**kwargs):
        self.name = name
        
        self.skills = args
        
        self.detail = kwargs

    def show_employee(self):
        print(f'{self.name}\n-{self.skills}\n-{self.detail}')


employe = Employee('Carlos','python','javascript','c++',age=30,city='Bogo')
employe.show_employee()