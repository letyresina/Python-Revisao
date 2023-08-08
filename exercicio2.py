'''
    Exercício 2
    Implemente a função quadrado que recebe um número e retorna o resultado desse número ao 
    quadrado.
'''

def aoQuadrado(num):
    quadrado = num ** 2
    return quadrado

num = float(input("Informe um número qualquer: "))
quadrado = aoQuadrado(num)

print(f"O número {num} ao quadrado é de {quadrado}")