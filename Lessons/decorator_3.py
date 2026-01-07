


#Decorador que comprueba si un empleado tiene un rol específico
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            #Si el rol de lempleado coincide con el rol requerido
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f'ACCESO DENEGAGO. Solo {required_role} pueden realizar esta acción')
        return wrapper
    return decorator

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

@check_access('admin')
@log_employee_action
def delete_employee(employee):
    return f"El empleado {employee['name']} ha sido elimiado"




admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

delete_employee(employee)
#delete_employee('empleado')
