def problem_1():
	'''Return the sum of all numbers divisble by 5 or 3 under 1000'''
	numbers = range(1000)
	result = 0
	for x in numbers:
		if x % 3 == 0 or x % 5 == 0:
			result += x

	return result

def problem_2():
	'''Return the sum of all even numbered fibonacci numbers under 4 million'''
	fibonacci = 3
	last = [1, 2]
	result = 2

	while last[1] <= 4000000:
		if fibonacci % 2 == 0:
			result += fibonacci
		fibonacci = last[0] + last[1]
		last = [last[1], fibonacci]

	return result

def problem_3(n):
	'''Returns the largest prime facotrs of a positive integer'''
	factors = []
	d = 2
	while n > 1:
		while n % d == 0:
			n /= d
		d += 1
		if d * d > n:
			if n > 1:
				return n