def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2,3,4,5,6,7,8,9,10))
               
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')



show_info(name='Juan',age=30,city='Bogo')    
show_info(name='Juan',age=30,city='Bogo',country='colombia')    
