'''
    Exercício 6
    Implemente a função soma_divisores, que recebe como parâmetro de entrada um número positivo 
    e retorna a soma de todos os divisores desse número.
    Por exemplo:
    - caso o número seja 15, o retorno deve ser 24 (1 + 3 + 5 + 15).
    - caso o número seja 30, o retorno deve ser 72 (1 + 2 + 3 + 5 + 6 + 10 + 15 + 30)
'''
 
def soma_divisores(num1):
        if num1 > 0:
            cont = 0
            for i in range(1, num1+1):
                if num1 % i == 0:
                    cont += i
            return cont  
        else:
            raise TypeError
    
try:
    num1 = int(input("Informe um número inteiro positivo: "))
    soma = soma_divisores(num1)
    print(f"A soma dos divisores do {num1} é de {soma}")
except TypeError:
        print("O programa aceita somente números positivos. Por favor, tente novamente.")