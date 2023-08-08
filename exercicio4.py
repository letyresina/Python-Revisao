'''
    Exercício 4
    Implemente a função media, que recebe três valores numéricos e retorna a média aritmética dos 
    valores.
'''

def calculaMedia(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media

num1 = float(input("Informe um número qualquer: "))
num2 = float(input("Informe outro número qualquer: "))
num3 = float(input("Informe outro número qualquer: "))

media = calculaMedia(num1, num2, num3)
print(f"A média aritmética dos números informados é de {media}")
