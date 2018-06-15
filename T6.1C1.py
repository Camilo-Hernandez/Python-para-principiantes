def sqrt(x, epsilon):
	'''Asume que x y epsilon son float,
	   que x>=0 y que epsion>0
	   Retorna resultado tal que:
	   x-epsilon <= resultado**2 <= x+epsilon'''

def isPrime(x):
	'''Asume que x es un entero no negativo
	   Retorna True si x es primo y Falso de lo contrario'''	
	if x <= 2:
		return False
	for i in range(2, x):
		if x%i == 0:
			return False
	return True