tempc = input('Informe a temperatura que deseja converter em Fahrenheit: \n')
c = eval(tempc)
tempf = (1.8*c)+32
print('O valor em Fahrenheit é: ', tempf)
print(f'O valor em Fahrenheit é: {tempf}')  # uso mais comum hoje.
print('O valor em Fahrenheit é: {}'.format(tempf))
