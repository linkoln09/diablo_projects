import random

words = ['identification', 'useless', 'drugdiller', 'magnus', 'anti-mage', 'ursa warrior']
word = list(random.choice(words))
word_user = []
for i in range(len(word)):
	word_user.append('_')

print(' '.join(word_user))

while ''.join(word_user) != ''.join(word):
	symbol_u = input('Write symbol: ')
	if symbol_u in word:
		for inx in range(len(word)):
			if symbol_u == word[inx]:
				word_user.insert(inx, word[inx])
				word_user.pop(inx + 1)
		print(' '.join(word_user))
	else:
		print('No symbol')
