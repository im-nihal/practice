#swapping logic using Temp/third Variable

#taking input from user
x = input("Enter Your Desired Number: ")
y = input("Enter Your Desired Number: ")

print("_____________________________________________")

#number entered by user
print("\nThe Value of x before Swapping: {}".format(x))
print("The Value of y before Swapping: {}".format(y))

temp = x
x = y
y = temp

print("\nThe Value of x after swapping: {}".format(x))
print("The Value of y after swapping: {}".format(y))

