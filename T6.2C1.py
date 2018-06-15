def isPal(x):
	'''Asume que x es una lista
	   Retorna True si x es palíndroma o Falso de lo contrario'''
	temp = x
	temp.reverse
	if temp == x:
		return True
	else:
		return False

def silly(n):
	'''Asume que n es un enter mayor que cero
	   Obtiene n entradas del ussuario
	   Imprime SI, si la palabra es palíndroma, NO de lo contrario'''
	
	for a in range(n):
		result = []
		elem = input('Ingrese elemento: ')
		result.append(elem)
	if isPal(result):
		print('SI')
	else:
		print('NO')