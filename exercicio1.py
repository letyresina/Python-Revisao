''' 
    Exercício 1
    Implemente a função somar que recebe dois números e retorna o resultado da soma desses dois números.
    Lembre-se que para retornar um resultado a função deve utilizar a instrução return.
'''

def soma(num1, num2):
    soma = num1 + num2
    return soma

num1 = float(input("Informe um número qualquer: "))
num2 = float(input("Informe outro número qualquer: "))

resultado = soma(num1, num2)
print(f"O resultado da soma de {num1} + {num2} é de {resultado}")