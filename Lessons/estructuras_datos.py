from collections import deque

def manage_delivery_queue() -> deque:

    #Se crea una cola para gestionar entregas de productos
    delivery_queue = deque(["order_1","order_2","order_3"])
    delivery_queue.append("order_4")#Al final de la cola se agrega 
    delivery_queue.appendleft("order_0") #Al principio de la cola
    delivery_queue.pop() #Elimina al final
    delivery_queue.popleft() #Elimina al final
    return delivery_queue
print(manage_delivery_queue())