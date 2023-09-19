def busca_binaria(lista, elemento):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        valor_meio = lista[meio]

        if valor_meio == elemento:
            return meio
        elif valor_meio < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 10]
elemento_procurado = 4
resultado = busca_binaria(lista, elemento_procurado)

if resultado != -1:
    print(f'O elemento {elemento_procurado} foi encontrado na posição {resultado}.')
else:
    print(f'O elemento {elemento_procurado} não foi encontrado na lista.')
