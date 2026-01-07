

def log_transaction(func):
    def wrapper():#envuelve a la funcion que se esta llamando
        print('1- Log de la transacsion.....')
        func()#se llama la funcion del argumento; ejecutandose todo dentro de process_payment
        print('3.Log terminado')
    return wrapper

@log_transaction#aqui usamos el decorador
def process_payment():
    print('2 - procesando pago ....')
    
process_payment()    