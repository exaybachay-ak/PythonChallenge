'''
fizzBuzz2.py

 As I remember it from my childhood, the way we played this, fizz was not only for numbers divisible by three, but also numbers containing a three. And buzz similarly for five. The really adventurous did something 
 similar for seven as well. -- JohnFletcher

 Ideas:
 Use toArray() function
 -evaluate each number in the array

num = 342
numStr = str(num)
'''

def printNums():
	num = 1
	numStr = str(num)

	while num < 10:
		if num % 3 == 0 and num % 5 == 0:
			print "FizzBuzz"
		elif num % 3 == 0:
			print "Fizz"
		elif numStr[0] == '3':
			print "Fizz"
		elif num % 5 == 0:
			print "Buzz"
		elif numStr[0] == '5':
			print "Buzz"
		else:
			print num
		num += 1
		numStr = str(num)

	while num >= 10 and num < 100:
		if num % 3 == 0 and num % 5 == 0:
			print "FizzBuzz"
		elif num % 3 == 0:
			print "Fizz"
		elif numStr[0] == '3':
			print "Fizz"
		elif numStr[1] == '3':
			print "Fizz"
		elif num % 5 == 0:
			print "Buzz"
		elif numStr[0] == '5':
			print "Buzz"
		elif numStr[1] == '5':
			print "Buzz"
		else:
			print num
		num += 1
		numStr = str(num)

printNums()
