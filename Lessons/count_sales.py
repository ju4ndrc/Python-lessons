from collections import Counter

def count_sales(products:list[str]) -> Counter:
    #Usa counter para contar cuantos productos de cada tipo se han vendido
    return Counter(products)

products = ['laptop', 'smartphone', 'smartphone', 'laptop', 'tablet']
result = count_sales(products)
print(result)  # Output: Counter({'laptop': 2, 'smartphone': 2, 'tablet': 1})