#!/usr/bin/env python3
#function computes factorial of a given number
def factorial(n):
	result = 1
	i=1
	while i<=n:
		result*=i
		i+=1
	return result
def test_answer():
    assert factorial(4) == 24

#read input from user
n = 5 #int(input('Enter a number: '))

#calculate factorial
result = factorial(n)

print(result)
