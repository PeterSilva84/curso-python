
sol= True   
calor= False

if sol and calor:
    print("Bora para praia!")

elif sol and not calor:
    print("Brora para o parque")
elif not sol and calor:
    print("Bora para a piscina")
elif not sol and not calor:
    print("House of dragon?")