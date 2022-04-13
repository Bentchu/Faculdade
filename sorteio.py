import random 
sorteio = random.randint(1,11) 
tentativa = 1
while tentativa < 5: 
	num=int(input('Adivinhe numero entre 1 e 10 ')) 
	tentativa+=1 
	if num==sorteio: 
		print('Parabéns! Você acertou!')
		break
	elif num < sorteio: 
		print('Número sorteado maior que o digitado.') 
	else: 
		print('Número sorteado é menor que o digitado.') 
print('Tentativas', tentativa-1) 
