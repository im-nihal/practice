# Binary Base Conversion Mechanism From Scratch

while True:
    print('Binary Base Conversion System')
    options = ['1. Binary To Decimal', '2. Binary To Octal', '3. Binary To Hex']
    for i in options:
        print(i)

    _input = int(input('\nEnter Your Choice: '))

    if _input == 1:
        print('-'*45)
        print(' ------ Binary To Decimal Conversion -------')
        print('-'*45)
        while True:
            try:
                bin_input = input("Please Enter Binary Number: ")
                if not all(char in ['0', '1'] for char in bin_input):
                    raise ValueError("Binary Number Consist 0's and 1's ONLY. Please Try Again!")
                
                result = 0
                for i in range(len(bin_input)):
                    result += int(bin_input[i]) * (2 ** (len(bin_input) - i - 1))
                print('The Decimal Equivalent of {} is = {}'.format(bin_input, result))
                break
            except ValueError as e:
                print(e)
                print('-'*45)
    
    elif _input == 2:
        print('-'*45)
        print(' ------ Binary To Octal Conversion -------')
        print('-'*45)
        while True:
            try:
                binNum = input("Enter Binary Number: ")
                if not all(char in ['0', '1'] for char in binNum):
                    raise ValueError("Binary Number Consist 0's and 1's ONLY.")
                
                while len(binNum) % 3 != 0: # Add leading zeros to make the binary number length divisible by 3
                    binNum = '0' + binNum
                    
                binGroups = [binNum[i:i+3] for i in range(0, len(binNum), 3)] # Split the binary number into groups of 3 digits
                # dictionary to map binary groups to octal digits
                binary_to_octal = {
                        '000': '0', '001': '1', '010': '2',
                        '011': '3', '100': '4', '101': '5',
                        '110': '6', '111': '7'
                        }
                
                # Convert each binary group to its octal equivalent
                octGroups = [binary_to_octal.get(i, '?') for i in binGroups]
                octal_number = ''.join(octGroups) # Join the octal groups to get the final octal number
                binNum = binNum.lstrip('0') # Remove leading zeros from the binary input number
                print(f"The Octal equivalent of {binNum} is = {octal_number}.")
                break
            
            except ValueError as e:
                print(e, '\nDo Not Enter AlphaNumeric Characters. Please Try Again!')
                print('-'*45)
                
        
    elif _input == 3:
        print('-'*45)
        print(' ------ Binary To Octal Conversion -------')
        print('-'*45)
        while True:
            try:
                binNum = input("Enter a Binary Num: ")
                if not all(char in ['0', '1'] for char in binNum):
                    raise ValueError("Binary Number Consist 0's and 1's ONLY.")

                # Add leading zeros to make the binary number length divisible by 4
                while len(binNum) % 4 != 0:
                    binNum = '0' + binNum

                # Split the binary number into groups of 4 digits
                binGroups = [binNum[i:i+4] for i in range(0, len(binNum), 4)]

                # Create a dictionary to map binary groups to hexadecimal digits
                binary_to_hex = {
                    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
                    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
                    }

                # Convert each binary group to its hexadecimal equivalent
                hexGroups = [binary_to_hex.get(i, '?') for i in binGroups]

                # Join the hexadecimal groups to get the final hexadecimal number
                hexNum = ''.join(hexGroups)

                # Remove leading zeros from the binary input number
                hexNum = hexNum.lstrip('0')

                # Print the hexadecimal number
                print(f"The hexadecimal equivalent of {binNum} is = {hexNum}.")
                break
            
            except ValueError as e:
                print(e, '\nDo Not Enter AlphaNumeric Characters. Please Try Again!')
                print('-'*45)

    print('='*45)
    repeat = input('Do you want to repeat again> (y/n): ')
    if repeat.lower() == 'n':
        print('\tSee You Again. BYE!')
        print('='*45)
        break
