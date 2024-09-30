from jaccard import jaccard_index

# Calcular o indice de 'Todo amor tem sua dor' e 'Toda vida tem seu valor', imprimindo a matriz
indice = jaccard_index('Todo amor tem sua dor', 'Toda vida tem seu valor', True)
print(f'Índice de Jaccard: {indice:.2f}')