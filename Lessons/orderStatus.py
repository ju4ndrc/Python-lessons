from enum import Enum

class OrderStatus(Enum):
    PENDING = 1 
    SHIPPED = 2 
    DELIVERED = 3

def check_status(status:OrderStatus):
    if status == OrderStatus.PENDING:
        return "Pendiente"
    elif status == OrderStatus.SHIPPED:
        return "Pagado"
    elif status == OrderStatus.DELIVERED:
        return "Entregado"
    
print(check_status(OrderStatus.PENDING))    
    
    