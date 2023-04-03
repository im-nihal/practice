# Octal Base Conversion Mechanism From Scratch

while True:
    print('Octal Base Conversion System')
    options = ['1. Octal To Binary', '2. Octal To Decimal', '3. Octal To Hex']
    for i in options:
        print(i)

    _input = int(input('\nEnter Your Choice: '))

    if _input == 1:
        print('-'*45)
        print(' ------ Octal To Binary Conversion -------')
        print('-'*45)
        while True:
            try:
                _octInput = input("Please Enter An Octal Number: ")

                # raising an exception to get the right input
                if not all(char in ['0', '1', '2', '3', '4', '5', '6', '7'] for char in _octInput):
                    raise ValueError("Octal Numbers Consist 0-7 digits ONLY.")

                # Defining dictionary of octal equivalent of binary numbers
                oct_to_binary = {
                        '0': '000', '1': '001', '2': '010',
                        '3': '011', '4': '100', '5': '101',
                        '6': '110', '7': '111'
                        }

                # converting each octal value to it's binary equivalent
                binNum = ""
                for i in _octInput:
                    binNum += oct_to_binary[i]

                # removing any leading zeros from the binary number
                binNum = binNum.lstrip('0')
                print("The Binary equivalent of octal({}) is = {}".format(_octInput, binNum))
                break
            except ValueError as e:
                print(e, '\nDo Not Enter AlphaNumeric Values.Please Try Again!')
                print('-'*45)
    
    elif _input == 2:
        print('-'*45)
        print(' ------ Octal To Decimal Conversion -------')
        print('-'*45)
        while True:
            try:
                # input from user
                _octInput = input("Please Enter An Octal Number: ")

                # raising an exception to get the right input
                if not all(char in ['0', '1', '2', '3', '4', '5', '6', '7'] for char in _octInput):
                    raise ValueError("Octal Numbers Consist 0-7 digits ONLY.")

                decNum = 0

                # converting octal digits to decimal
                for i in range(len(_octInput)):
                    digit = int(_octInput[len(_octInput) - i - 1])
                    decNum += digit *(8**i)
                    
                print(f"The Decimal equivalent of octal({_octInput}) is = {decNum}.")
                break
            
            except ValueError as e:
                print(e, '\nDo Not Enter AlphaNumeric Values. Please Try Again!')
                print('-'*45)
                
        
    elif _input == 3:
        print('-'*45)
        print(' ------ Octal To HexDec Conversion -------')
        print('-'*45)
        while True:
            try:
                _octInput = input("Please Enter An Octal Number: ")

                # raising an exception to get the right input
                if not all(char in ['0', '1', '2', '3', '4', '5', '6', '7'] for char in _octInput):
                    raise ValueError("Octal Numbers Consist 0-7 digits ONLY.")


                # Converting octal num to decimal
                _decimal = 0
                for i in range(len(_octInput)):
                    digit = int(_octInput[len(_octInput)- i - 1])
                    _decimal += digit* (8**i)

                # Convert decimal num to hexadecimal
                _hexNum = ""
                _hexDigits = "0123456789ABCDEF"
                while _decimal > 0:
                    remainder = _decimal % 16
                    _hexNum = _hexDigits[remainder] + _hexNum
                    _decimal //= 16

                print(f"The Hexadecimal Equivalent of octal({_octInput}) is = {_hexNum}")
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
