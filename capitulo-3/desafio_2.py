
a = int(input("Medida do primeiro lado: "))
b = int(input("Medida do segundo lado: "))
c = int(input("Medida do terceiro lado: "))

if a + b > c or b + c > a or a + c > b:
    print("É um triangulo!")
    if a == b == c:
        print("Triangulo equilátero")
    elif a == b or b == c or a == c:
        print("Isósceles")
    elif a != b or b != c or c != a:
        print("Escaleno")



