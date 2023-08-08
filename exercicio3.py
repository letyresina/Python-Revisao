'''
    Exercício 3
    Implemente a função soma_dos_quadrados que receba dois numeros e devolve a soma dos seus 
    quadrados.
    Você pode tentar reutilizar a função quadrado definida anteriormente para facilitar a implementação.
'''

def soma_dos_quadrados(num1, num2):
    soma = (num1 ** 2) + (num2 ** 2)
    return soma

num1 = float(input("Informe um número qualquer: "))
num2 = float(input("Informe outro número qualquer: "))

soma = soma_dos_quadrados(num1, num2)
print(f"A soma dos quadrados dos números {num1} e {num2} é de {soma}")