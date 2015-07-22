def problem_1:
	'''Return the sum of all numbers divisble by 5 or 3 under 1000'''
	numbers = range(1000)
	result = 0
	for x in numbers:
		if x % 3 == 0 or x % 5 == 0:
			result += x

	return result