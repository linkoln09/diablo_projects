x = 0
y = ['*']

while x < 4:
	print(' '.join(y))
	y.append('*')
	x += 1

while x > -1:
	print(' '.join(y))
	y.pop()
	x -= 1
	
	
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
    
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


for i in range(1,10):
	print("* " * int(5 - abs(i - 5)))
