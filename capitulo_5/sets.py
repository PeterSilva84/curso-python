s1 = {1, 2, 3, 4, 5}

print(s1)
print(type(s1))

s2 = {4, 5, 6, 7, 8}

print(s2)

u = s1.union(s2)
#juntamos as duas tabelas e  ele printa todos os números somente 1 vez
print(u)

i = s1.intersection(s2)

print(i)

s1.add('item novo')

print(s1)

d= s1.difference(s2)

print(d)

print(s1.clear())

