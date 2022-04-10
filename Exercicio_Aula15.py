#Exercício pedido em aula - média de notas - aprovação

n1 = eval(input('Entre com a primeira nota: '))
n2 = eval(input('Entre com a segunda nota: '))

media = 0.4*n1 + 0.6*n2

if media >= 5:
	print('Sua média é ', media, ' e você está aprovado(a)\n')
else:
	print('Sua média é ', media, ' e você está reprovado(a)\n')

