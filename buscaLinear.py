def buscaLinear(lista, num):
    for i in lista:
        if num == lista[i]:
            print("O numero esta presente na lista")

buscaLinear([1,2,3,4], 2)