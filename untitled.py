import string

upper_case = string.ascii_uppercase 
print(string.ascii_lowercase)
print(string.digits)


def sort(my_list):
	for number in range(len(my_list)):
		for i in range(len(my_list) - 1, number, -1):
			if my_list[i] < my_list[i-1]:
				my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
	print(my_list)


sort(['a', 'f', 'b'])
sort([2, 4, 1, 0, 8, 5, 3, 9, 23])

print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')

digit_list = [2, 5, 8, 4, 10, 6, 3, 11, 23, 22]

for i in digit_list:
	if i % 2 == 0:
		print(i)

print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
		
random_list = ['s', 2, 'f', 3, 'd', 4, 2, 'y']

for rdl in random_list:
	if isinstance(rdl, int):
		print(rdl)

print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')


print(digit_list[::-1])

for inx in range(len(random_list)):
	if not isinstance(random_list[inx], str):
		random_list[inx] = str(random_list[inx])
		
print(random_list)

if type(a) == str:
	return True
	
