def sem_repetidos(lista1, lista2):
    
    lista_resultante = list(set(lista1 + lista2))
    return lista_resultante

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

resultado = sem_repetidos(lista1, lista2)

print("Lista resultante sem elementos repetidos:", resultado)
