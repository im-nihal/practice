# Hexadecimal Base Conversion Mechanism From Scratch

while True:
    print('Hexadecimal Base Conversion System')
    options = ['1. Hex To Binary', '2. Hex To Decimal', '3. Hex To Octal']
    for i in options:
        print(i)

    _input = int(input('\nEnter Your Choice: '))

    if _input == 1:
        print('-'*45)
        print(' ------ Hexadecimal To Binary Conversion -------')
        print('-'*45)
        while True:
            try:
                _hex = input("Please Enter An HEX Number: ")

                # raising an exception to get the right input
                if not all(char.isdigit() or char.lower() in 'abcdef' for char in _hex):
                    raise ValueError("Hex Digits Consist 0-9 digits & A-F or a-f alphabets ONLY.")

                # Defining dictionary of octal equivalent of binary numbers
                hex_to_binary = {
                    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
                    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
                    'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 
                    'e': '1110', 'f': '1111'
                }

                # converting each hex group to it's binary equivalent           
                binGroups = [hex_to_binary.get(i, '?') for i in _hex]
                binNum = ''.join(binGroups)

                # removing any leading zeros
                binNum = binNum.lstrip('0')
                print(f"The Binary Equivalent of Hex({_hex}) is = {binNum}")
                break
            
            except ValueError as e:
                print(e, "\nConsist 'A-F' alphabets ONLY.Please Try Again!")
                print('-'*45)
    
    elif _input == 2:
        print('-'*45)
        print(' ------ Hexadecimal To Decimal Conversion -------')
        print('-'*45)
        while True:
            try:
                # input from user
                _hex = input("Please Enter An Hexadec Number: ")

                # raising an exception to get the right input
                if not all(char.isdigit() or char.lower() in 'abcdef' for char in _hex):
                    raise ValueError("Hex Digits Consist 0-9 digits & A-F or a-f alphabets ONLY.")

                # convert each digit to decimal equivalent using int() function
                decEquiv = 0
                for i, digit in enumerate(reversed(_hex)):
                    decEquiv += int(digit, 16) * (16 ** i)
                    
                print(f"The Decimal Equivalent of Hex({_hex}) is = {decEquiv}")
                break
            
            except ValueError as e:
                print(e, '\nDo Not Enter AlphaNumeric Values. Please Try Again!')
                print('-'*45)
                
        
    elif _input == 3:
        print('-'*45)
        print(' ------ Hexadecimal To Octal Conversion -------')
        print('-'*45)
        while True:
            try:
                # input from user
                _hex = input("Please Enter A Hexadecimal Number: ")

                # raising an exception to get the right input
                if not all(char.isdigit() or char.lower() in 'abcdef' for char in _hex):
                    raise ValueError("Hex Digits Consist 0-9 digits & A-F or a-f alphabets ONLY.")

                # convert hex string to binary string
                binEquiv = bin(int(_hex, 16))[2:]

                # pad binary string with leading zeros to ensure groups of 3 bits
                while len(binEquiv) % 3 != 0:
                    binEquiv = '0' + binEquiv

                # group binary string into groups of 3 bits and convert to octal
                octEquiv = ''
                for i in range(0, len(binEquiv), 3):
                    binGroup = binEquiv[i:i+3]
                    octDigit = str(int(binGroup, 2))
                    octEquiv += octDigit

                print(f"The Octal Equivalent of Hex({_hex}) is = {octEquiv}")
                break
            
            except ValueError as e:
                print(e, '\nDo Not Enter AlphaNumeric Characters.  Please Try Again!')
                print('-'*45)

    print('='*45)
    repeat = input('Do you want to repeat again> (y/n): ')
    if repeat.lower() == 'n':
        print('\tSee You Again. BYE!')
        print('='*45)
        break
