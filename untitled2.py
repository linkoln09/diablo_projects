import string
import random

def random_pass_choice():
	symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
	password_list = []

	length_pass = input('Введите длину пароля: ')

	for idx in range(int(length_pass)):
		password_list.append(random.choice(symbols))
	
	password = ''.join(password_list)
	print(password)
	
random_pass_choice()


def random_pass_sample():
	symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits

	length_pass = input('Введите длину пароля: ')
	
	password = random.sample(symbols, int(length_pass))
	password = ''.join(password)
	print(password)

random_pass_sample()


