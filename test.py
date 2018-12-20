#this is a test

num = input("input a number: ")
check = input("input a second number to divide it by the first number")
num = int(num)
check = int(check)
if num % 4 == 0:
	print("%s is an even number that is divisble by 4" % num)
elif num % 2 == 0:
	print("%s is an even number" % num)
else:
	print("%s is an odd number" % num)
