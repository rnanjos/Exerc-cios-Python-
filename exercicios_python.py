'''
	Exercício de repetição - enquanto o usario não digitar 0 o programa sempre solicitará um numnero
'''
soma = 0
while True:
    x = int(input("Digite o número (0 sai): "))
    if x == 0:
        break
    soma = soma + x
print ("Soma: %d" %soma)

'''
	Exercício de repetição - Imprimir apenas numeros pares

'''
x = 1
while True:
    if x % 2 == 0:
        print(x)
    x = x + 1

'''
	Acumuladores - Cálcule a média de 10 números inteiro
'''
n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o %d número: " %n))
    soma = soma + x
    n = n + 1
print("Média: %5.2f" %(soma/10))

'''
	Calcule o fatorial de um número inteiro 
'''
i = 1
x = 1
fat = int(input("Digite um numero"))
while i <= fat:
    x = x * i
    i = i+ 1
print("Fator(%d) = %d"%(fat, x)) 
    