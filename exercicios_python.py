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
