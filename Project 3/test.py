import numpy as np
import matplotlib.pyplot as plt
from math import factorial, exp

def problem_2():
	binomial = lambda n, p, q, x : ((factorial(n) // (factorial(x) * factorial(n - x))) * (p**x) * (q**(n - x)))
	n = 1000		# number of trials
	p = 1/216		# probability of success: 3 sixes in a single roll of 3 fair die
	q = 1 - p		# probability of failure

	X = [binomial(n, p, q, x) for x in range(0, 21)]
	print (*X, sep='\n')

	'''
	b = range(1, 18)
	h1, bin_edges = np.histogram(X, bins = b)
	b1 = bin_edges[0 : 16]
	fig1 = plt.figure(1)
	plt.stem(b1, h1)
	plt.title('Probability of rolling three 6\'s using Binomial')
	plt.xlabel('Number of rolls')
	plt.ylabel('Probability')
	fig1.savefig('test.png')
	'''

	plt.stem(X, bins = 16)
	plt.title('Test 2')
	plt.xlabel('Number of rolls')
	plt.ylabel('Probability')
	plt.show()

def problem_3():
	poisson = lambda l, x: ((l**x) * exp(-l)) / factorial(x)
	n = 1000
	p = 1/216		
	q = 1 - p		
	l = n * p

	X = [poisson(l, x) for x in range(0, 21)]
	print(*X, sep='\n')

	plt.stem(X, bins = 16)
	plt.title('Test 3')
	plt.xlabel('Number of rolls')
	plt.ylabel('Probability')
	plt.show()

problem_3()