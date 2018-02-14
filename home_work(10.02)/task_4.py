row_count = int(input('Введите количество строк: '))
col_count = int(input('Введите количество столбцов: '))

two_dimen_array = [[0 for col in range(col_count)] for row in range(row_count)]

for row in range(row_count):
	for col in range(col_count):
		two_dimen_array[row][col] = row*col


print(two_dimen_array)
