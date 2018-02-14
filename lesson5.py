dictionary_user = {
	'dima': '1234', 
	'igor': '4321'
}

username = input('User name: ')
if not username:
	raise RuntimeError('Username is empty')
user_password = input('Password: ')


try:
	authenticate = dictionary_user[username] == user_password
	if not authenticate:
		print('Password is incorrect')
except KeyError:
	print('User not finde')
