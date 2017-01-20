from array import array
tal = input("ange dintal: ").split()
lista = array('l')

for value in tal:
    lista.append(int(value))

print(lista)
