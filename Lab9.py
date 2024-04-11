def encode(password):
	en = ""
	for key in password:
		dig = str(int(key) +3 )
		en += dig
	return en

def main():
    while True:
        print('Menu\n'
            '-------------\n'
            '1. Encode\n'
            '2. Decode\n'
            '3. Quit\n')

        option = input('Please enter an option: ')
        if option == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n')



        if option == '3':
            break

if __name__ == '__main__':
    main()