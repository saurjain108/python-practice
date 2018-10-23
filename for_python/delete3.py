fact = 1
def factorial(n):
	if n==0 or n==1:
		return (1)
	else:
		return (n * factorial(n-1))


print(factorial(5))

def fact(n):
	total = 1
	while n>=1:
		total = total*n
		n=n-1
	return total

print(fact(5))
	
