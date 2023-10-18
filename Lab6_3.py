def general(m):

    result = m[0]


    for shop in m[1:]:
        result = result.intersection(shop)
    

    
    return result

# Приклад використання
m1 = {'морква', 'шоколад', 'риба'}
m2 = {'морозиво', 'риба', 'морква'}
m3 = {'картопля', 'морква', 'риба'}

m = [m1, m2, m3]

result = general(m)
print(f"Спільний асортимент продуктів: {result}")