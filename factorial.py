# -*- coding: utf-8 -*-

#programa ejemplo de recursion
def factorial(num):
    if num < 2:
        return 1
    else:
	return num*factorial(num-1)


def run():
    num = int(raw_input('Escribe el numero: '))
    result = factorial(num)	
    print('Factorial es: {}').format(result)	

if __name__ == '__main__':
	run()