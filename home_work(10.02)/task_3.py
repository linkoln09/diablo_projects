num_s = input('Введите числа через пробел: ')
num_l = num_s.split(' ')
num_even = []
num_odd = []


for num in num_l:
		if int(num) % 2 == 0:
			num_odd.append(num)
		else:
			num_even.append(num)

	
print('Количество нечетных чисел: ' + str(len(num_even)))
print('Количество четных чисел: ' + str(len(num_odd)))
