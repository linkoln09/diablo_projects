info = input('Введите строку: ')
alpha = []
digit = []


for i in info:
		if i == ' ':
			continue
		elif i.isdigit():
			digit.append(i)
		elif i.isalpha():
			alpha.append(i)


print('Количество букв: ' + str(len(alpha)))
print('Количество чисел: ' + str(len(digit)))
