'''
    Exercício 5
    Implemente a função calcular_salario, que recebe o salário atual de um funcionário e retorna o salário com um 
    reajuste de aumento, sendo que:
    - Caso o salário seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento.
    - Caso contrário, o funcionário receberá 15% de aumento.
'''

def calcular_salario(salario):
    if salario >= 2000:
        porcentagem = salario * 0.07
    else:
        porcentagem = salario * 0.15

    aumento = salario + porcentagem
    return aumento

salario = float(input("Olá usuário! Por favor, informe-nos o seu salário atual: "))

print(f"Parabéns pelo aumento! Você recebia {salario}, e agora, você recebe {calcular_salario(salario)}!")
