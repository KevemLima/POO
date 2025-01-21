# Lista inicial
numeros = [5, 10, 15, 30, 45]

# Passo 1: Adicionar o número 15 ao final da lista
numeros.append(15)

# Passo 2: Inserir o número 20 na segunda posição
numeros.insert(1, 20)

# Passo 3: Remover o primeiro número da lista
numeros.pop(0)

# Passo 4: Verificar se o número 10 está presente e substituir por 25
if 10 in numeros:
    indice_10 = numeros.index(10)
    numeros[indice_10] = 25

# Passo 5: Calcular a média dos números na lista
media = sum(numeros) / len(numeros)

# Exibir a média
print(f"Média dos números na lista: {media}")

# Passo 6: Exibir a lista final
print(f"Lista final: {numeros}")