# Max of three numbers

def max_three(a, b, c):
	if a > b and a > c:
		return a
	elif b > a and b > c:
		return b
	else:
		return c

#print(max_three(-9, -1, -3))

# sum of list

def sum_lst(a):
	sum_l = 0
	for i in a:
		sum_l += i
	return sum_l
	
#print(sum_lst([5, 4, 1, 7, -5, 3]))
	
# multiply of list

def mul_lst(a):
	mul_l = 1
	for i in a:
		mul_l *= i
	return mul_l

#print(mul_lst([9, 2, 3, -5]))

#revers string

def reverse_str(a):
	b = a[::-1]
	return b

print(reverse_str('dfnn3kk30fdnn3jhjkdhjk3'))
