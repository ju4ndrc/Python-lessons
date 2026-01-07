def check_access(func):
    def wrapper(employee):
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('Dennied access')
    return wrapper

def log_employee_action(func):
    def wrapper(employee):
        result = func(employee)
        with open('employee.txt',mode='a') as f:
            f.write('\n')
            f.write('Iniciando seguimiento')
            f.write(f'El empleado :{result} ')
            print('Accion registrada')
        return result
    return wrapper

        

@log_employee_action
def delete_employee(employee):
    return f"El empleado {employee['name']} ha sido elimiado"

admin = {'name': 'Carlos', 'role': 'admin'}
empleado = {'name': 'Ana', 'role': 'empleado'}

delete_employee(admin)
# delete_employee(empleado)    