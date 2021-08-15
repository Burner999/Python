
number=input("Enter a number to determine if it is even or odd, also I'll tell you if it is a multiple of ten: ")
number=int(number)
if number%2 ==0:
	print("This number is even")
else:
	print("This number is odd")


if number%10 ==0:
	print("This number is a multiple of 10")
else:
	print("This number is not a multiple of 10")
