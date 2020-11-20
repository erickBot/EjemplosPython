#-*- coding:utf-8 -*-

#importamos libreria random
import random

def run():
    number_found = False
    randon_number = random.randint(0,range_end)

    while not number_found:
        number = int(raw_input('Intenta un numero: '))
        
	if number == randon_number:
	    print('Felicidades encontraste el numero')
	    number_found = True

	elif number > randon_number:
	    print('El numero es mas pequeno')
	else:
	    print('El numero es mas grande')
	



if __name__ == '__main__':
    range_end = int(raw_input('ingrese el rango: '))
    run()
