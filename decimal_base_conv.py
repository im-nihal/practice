while True:
    print('-------------------Options-------------------')
    choice = ['1. Decimal To Binary', '2. Decimal To Octal', '3. Decimal To Hex']
    print()
    for i in choice:
        print(i)

    usr_input = int(input('\nEnter the Your Choice: '))

    if usr_input == 1:
        print('-'*45)
        print('Decimal To Binary Conversion')
        print('-'*45)
        while True:
            try:
                dec_num = int(input("Please Enter A Decimal Number: "))
                num = dec_num
                remainders = []
                while dec_num > 0:
                    remainder = dec_num % 2
                    remainders.append(str(remainder))
                    dec_num //= 2
                bin_num = ''.join(remainders[::-1])
                print('The Binary Equivalent of {} is = {}'.format(num, bin_num))
                break
            except ValueError as invalid:
                print('-'*45)
                print(invalid)
                print('Please Do Not Enter Alphanumeric Characters.')
                print('-'*45)

    elif usr_input == 2:
        print('-'*45)
        print('Decimal To Octal Conversion')
        print('-'*45)
        while True:
            try:
                dec_num = int(input("Please Enter A decimal Number: "))
                num = dec_num
                remainders = []
                while dec_num > 0:
                    remainder = dec_num % 8
                    remainders.append(str(remainder))
                    dec_num //= 8
                oct_num = ''.join(remainders[::-1])
                if len(oct_num) == 0:
                    oct_num = '0'
                print('The Octal Equivalent of {} is = {}'
                      .format(num, oct_num.zfill(len(oct_num) + (3 - len(oct_num) % 3) % 3)))
                break
            except ValueError as invalid:
                print('-'*45)
                print(invalid)
                print('Please Do Not Enter Alphanumeric Characters.')
                print('-'*45)

    elif usr_input == 3:
        print('-'*45)
        print('Decimal To Hexadecimal Conversion')
        print('-'*45)
        while True:
            try:
                dec_num = int(input("Please Enter A Decimal Number: "))
                num = dec_num
                remainders = []
                while dec_num > 0:
                    remainder = dec_num % 16
                    if remainder < 10:
                        remainders.append(str(remainder))
                    else:
                        remainders.append(chr(remainder + 55))
                    dec_num //= 16
                hex_num = ''.join(remainders[::-1])
                print('The Hexadecimal Equivalent of {} is = {}'
                      .format(num, hex_num.zfill(len(hex_num) + (3 - len(hex_num) % 3) % 3)))
                break
            except ValueError as invalid:
                print('-'*45)
                print(invalid)
                print('Please Do Not Enter Alphanumeric Characters.')
                print('-'*45)
                

    print('='*45)
    repeat = input("Do you want to repeat again? (y/n): ")
    if repeat.lower() == "n":
        print('='*40)
        print('Thank You For Using Our Service.')
        break
