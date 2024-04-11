
#Veronica Ocampo
def encode(password):
	en = ""
	for key in password:
		dig = str(int(key) +3 )
		en += dig
	return en

def decode(password):
    passw = str(password)
    decoded = ''
    for i in range(len(passw)):
        b = int(passw[i]) + 3
        decoded += str(b)

    return decoded

#Tonuka Sultan
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

        if option == '2':
            print(f'The encoded password is {encoded_password}, and the original password is {password}.')


        if option == '3':
            break

if __name__ == '__main__':
    main()