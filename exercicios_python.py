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
    i = i + 1
print("Fator(%d) = %d" %(fat, x)) 

'''
	Tabuada
'''
tabuada = 1
while tabuada <= 10:
    n = 1
    print("Tabuada %d" %tabuada)
    while n <= 10:
        print("%d x %d = %d" %(tabuada, n, tabuada * n))
        n = n + 1
    tabuada = tabuada + 1

'''
	Ler três números e mostrar o maior 
'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 >= n2 and n1 >= n3:
         print("%d é maior" %n1)
elif n2 >= n1 and n2 >= n3:
         print("%d é maior" %n2)
else:
     print("%d é maior" %n3)   
         
'''
    Lista -  Calcule a média de 5 notas
'''
nota = [10, 8, 6, 5, 7.5]
i = 0
soma = 0
while i < 5:
    soma = soma + nota[i]
    i = i + 1;
print(" A média é %5.2f" %(soma/5))

'''
    Lista -  Programa que lê 5 números inteiros 
'''
i = 0
nota = []
while i < 5:
    x = int(input("Digite um numero: "))
    nota.append(x)
    i += 1
print(nota)

'''
    Listas -  Programa que lê um vetor de dez números reais e mostre-os na ordem inversa
'''
i = 0
numero = []
while i < 10:
    x = int(input("Digite um numero: "))
    numero.append(x)
    i += 1
i = 9
while i >= 0:
    print(numero[i])
    i -= 1
    
'''
	Lista - Programa que lê quatros notas e mostra a média na tela
'''
i = 1
notas = []
while i <= 4:
    n = int(input("Digite a %dº nota: " %i))
    notas.append(n)
    i += 1
soma = 0
i = 0
while i <= 3:
    soma = soma + notas[i]
    i += 1
print("A média é %4.2f" %(soma/4))

'''
    Programa que lê um vetor de 10 caracteres minúsculos, e diga quantas cosoantes foram lidas
'''
lista = []
i = 1
while i <= 10:
    x = input( 'Letra: ')
    lista.append(x)
    i += 1
i = 0
cont = 0
while i <= 9:
    if lista[i] not in 'aeiou':
        cont += 1
    i += 1
print("Foram lidos %d consoantes" %cont)

