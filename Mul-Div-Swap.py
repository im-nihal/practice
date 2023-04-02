#swapping logic with Multiplication & Division

#taking input from user
x = int(input("Enter Your Desired Number: "))
y = int(input("Enter Your Desired Number: "))
print("_____________________________________________")

#number entered by user
print("\nThe Value of x before Swapping: {}".format(x))
print("The Value of y before Swapping: {}".format(y))

x = x * y
y = x / y
x = x / y

print("\nThe Value of x after swapping: {}".format(x))
print("The Value of y after swapping: {}".format(y))
