import random

class AccountBanck:
    def __init__(self,name,amount = 0):
        
        self.name = name
        self._amount = amount
        

    def __str__(self):
        return f'{self.name} '
    def _update_amount(self,amount):
        self._amount = self._amount + amount

    def __register_transaction(self,transaction):
        self.__transactions[transaction._amount] = transaction
    def transactions(self,quantity):
        self._update_amount(quantity)
        self.__register_transaction(quantity)

    def show_transactions(self):
        print(f'\n{self.__transactions}')

class DbTransactions:
    def __init__(self):
        self.__transactions = {}
        # Ya cree la clase para usar como base de datos
new1 = AccountBanck('Juan',90)

new1.transactions(90)
        
new1.show_transactions()

