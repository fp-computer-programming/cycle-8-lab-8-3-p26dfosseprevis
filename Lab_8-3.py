"""
Create a Python file named lab_8-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***
Create a Python file named lab_8-3.py
Write the while-loop version of the following for-loop program.

def sum_to(n):
  total = 0
	for i in range(n+1):
		total += i
	return total

The function should be able to have an integer passed to it and return the sum of all the values from 1 to that integer
"""
def sum_to(n):
	total = 0
	i = 0
	while i <= n:
		total += i
		i += 1
	return total

print(sum_to(3))
print(sum_to(7))
print(sum_to(4))