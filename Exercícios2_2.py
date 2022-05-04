#Exercício 2.2
#Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:
#(a) A soma de 2 e 2 é menor que 4.
#(b) O valor de 7 // 3 é igual a 1 + 1.
#(c) A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
#(d) A soma de 2, 4 e 6 é maior que 12.
#(e) 1387 é divisível por 19.
#(f) 31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
#(g) O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*

soma = 2 + 2
if soma < 4:
	print ('True')
else:
	print ('False')	

divide = (7 // 3)
soma = (1 + 1)
if divide == soma:
	print ('True')
else:
	print ('False')
	
potencia1 = 3 ** 2
potencia2 = 4 ** 2
if potencia1 + potencia2 == 25:
	print ('True')
else:
	print ('False')

soma = 0
soma = 2 + 4 + 6
if soma > 12:
	print ('True')
else:
	print ('False')	

divide = 0
divide = 1387 % 19
if divide == 0:
	print ('True')
else:
	print ('False')
	
divide = 0
divide = 31 % 2
if divide == 0:
	print ('True')
else:
	print ('False')
	
precos = [34.99, 29.95, 31.50]	
menorpreco = min(precos)
if menorpreco < 30:
	print ('True')
else:
	print ('False')
	
