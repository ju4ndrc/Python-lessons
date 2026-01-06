from enum import Enum 
from collections import defaultdict
from collections import deque
import random
from collections import Counter

class OrderStatus(Enum):
    PENDDING=1
    SHIPPED=2  
    DELIVERED=3  


def check_status(status:OrderStatus):
    if status == OrderStatus.PENDDING:
        return "Pendiente"
    elif status == OrderStatus.SHIPPED:
        return "Pagado"
    elif status == OrderStatus.DELIVERED:
        return "Entregado"
    else:
        return "Orden no encontrada"

def create_order(products:list[str])-> defaultdict:

    order = []
    
    status = OrderStatus.PENDDING
    op = 1
    
    while(op != 0 ):
        print("Seleccione un producto para su orden \n")
        for i , product in enumerate(products):
            print(f"{i+1} - {product} \n")
        select_product = int(input("Que producto desea ingresar a su orden? \n"))
        order_product = products[select_product-1]
        order.append(order_product)

        op = int(input("Desea salir? = 0"))
    # status = 1
    # order.append(status)    
    return {
        "products":order,
            "status":status
            }





def count_sales(products:list[str]) -> Counter:
    #Usa counter para contar cuantos productos de cada tipo se han vendido
    return Counter(products)



products = ['laptop', 'smartphone', 'tablet']

order = create_order(products)

count = count_sales(order)

print(order)
print(count)




