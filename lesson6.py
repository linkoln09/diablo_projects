list1 = [x for x in range(10)]
list2 = [x for x in range(0, 10, 2)]
list3 = []

def intersection1(a, b, c):
	for i in a:
		if i in b:
			c.append(i)
	print(c)

intersection1(list2, list1, list3)

def intersection2(a, b):
	s1 = set(a)
	s2 = set(b)
	c = s1 & s2
	print(c)
	
intersection2(list1, list2)
