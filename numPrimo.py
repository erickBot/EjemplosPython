# -*- coding: utf-8 -*-

def is_prime(num):
    if num < 2:
	return False
    elif num == 2:
	return True
    elif num > 2 and num % 2 == 0:
	return False
    else:
	for i in range(3, num):
	    if num % i == 0:
		return False
	    
    return True
   	

def run():
    num = int(raw_input('Escribe un numero: '))
    result = is_prime(num)
	
    if result is True: 
	print('Tu numero es primo')
    else:
	print('Tu numero no es primo')
 


if __name__ == '__main__':
    run() 
