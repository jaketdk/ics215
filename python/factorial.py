def factorial(num):
	temp = num - 1
	retVal = num
	while temp > 0:
		retVal = retVal * temp
		temp = temp - 1
	return retVal

number = input('What number would you like to find the factorial of? ')
answer = factorial(number)

print "The factorial is", answer
