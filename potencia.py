def potencia(base,expoente): 
       resultado = 1 
       for numero in range(1,expoente+1): 
           resultado = resultado * base 
       return resultado 

numero = eval(input("Entre um número que quer calcular (base): ")) 
expoente = eval(input("Entre o expoente: ")) 
print( 'Potencia : ' ,potencia(numero,expoente)) 
