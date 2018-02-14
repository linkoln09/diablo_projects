import os

countries = {'Ukraine': 'UA', 'Russia': 'RU', 'Belarus': 'BY', 'Poland': 'PL', 'Lithuania': 'LI'}
domain_capitals = {'UA': 'Kiev', 'RU': 'Moscow', 'BY': 'Minsk', 'PL': 'Warsaw', 'LI': 'Vilnius'}

for county, domain in countries.items():
	print(county + ': ' + domain_capitals[domain])



my_set1 = {3, 4, 5, 3, 2, 4, 7}
my_set2 = {5, 2, 1, 2, 1, 5, 6, 9, 3, 4}
my_set3 = my_set1 & my_set2
my_set4 = my_set1 - my_set2
print(my_set1)
print(my_set2)
print(my_set3)
print(my_set4)
print(tuple(my_set1)[0:3])
print(tuple(my_set2)[::-1])

inp = open('document', 'w')
inp.write('Hello!\n')
inp.close()
inp = open('document')
print(inp.read())
inp.close()
inp = open('document', 'a')
inp.write('Good luck!\n')
inp.close()
inp = open('document')
print(inp.read())
inp.close()



with open('myfile.txt', 'w') as f:
	f.write('Hello file world!')
	
with open('myfile.txt') as f:
	print(f.read())

with open('myfile.txt', 'a') as f:
	f.write('\nHello my file!')

with open('myfile.txt') as f:
	print(f.read())
