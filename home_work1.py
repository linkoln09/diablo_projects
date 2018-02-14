def ascii_symblos():
    user_text = input('Write your text: ')
    
    print('Your text: ' + user_text + '\nFirst symbol: ' +
           user_text[0] + '\nASCII code of first symbol: ' + 
           str(ord(user_text[0])))
    print('\n/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/\n')
    print('ASCII symbols of all user\'s text: ')
    for a in user_text:
        print(a + ' is ' + str(ord(a)) + ' in ASCII')


ascii_symblos()
