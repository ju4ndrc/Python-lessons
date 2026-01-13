import random

class AccountBanck:
    def __init__(self,id,name,amount = 0):
        self.id = id
        self.name = name
        self._amount = amount
        self.__transactions = {}
        

    def __str__(self):
        return f'{self.name} '
    
    def __register_transaction(self,transaction):

        self.__transactions[transaction.id] = transaction
    
    def _update_amount(self,amount):
        self._amount = self._amount + amount


    def deposit(self,quantity):
        


        

    def withdraw(self,quantity):
        
        if self._amount < quantity:
            return 'Monto insuficiente'
        else:
            self._amount -= quantity

    def show_amount(self):        





