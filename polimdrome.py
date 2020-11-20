#-*- coding: utf-8 -*-

def polindrome(word):
    #declara variable inicial y vacia
    reversed_letters = []

    for letter in word:
	reversed_letters.insert(0,letter)
        #print(reversed_letters)

    #metodo 'join' une los caracteres de un string
    reversed_word = ''.join(reversed_letters)
    print(reversed_word)  

    if reversed_word == word:
	return True
    else:
	return False


def run():
    word = str(raw_input('Ingrese una palabra: '))
    result = polindrome(word)
    
    if result == True:
	print('Su palabra es palindrome')
    else:
        print('Su palabra no es palindrome')
 

if __name__ == '__main__':
	run()
