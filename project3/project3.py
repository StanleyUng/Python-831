import numpy as np
import matplotlib.pyplot as plt
from math import factorial, exp

def problem_1(N):
	n = 1000
	success = [sum([int(sum([np.random.randint(1, 7) for i in range(0, 3)]) == 18) for i in range(0, n)]) for i in range(0, N)]
	b = range(1, 18)
	h1, bin_edges = np.histogram(success, bins = b)
	b1 = bin_edges[0 : 16]
	fig1 = plt.figure(1)
	plt.stem(b1, h1/N)
	plt.title('Exoerimental Results: Problem 1')
	plt.xlabel('Number of successes in n = 1000 trials')
	plt.ylabel('Probability of success')
	plt.savefig('PMF.png')


def problem_2():
	binomial = lambda n, p, q, x : ((factorial(n) // (factorial(x) * factorial(n - x))) * (p**x) * (q**(n - x)))
	n = 1000
	p = 1/216
	q = 1 - p
	X = [binomial(n, p, q, x) for x in range(0, 21)]
	plt.stem(X, bins = range(1, 18))
	plt.title('Exoerimental Results: Problem 2')
	plt.xlabel('Number of successes in n = 1000 trials')
	plt.ylabel('Probability of success')
	plt.savefig('Binomial.png')


def problem_3():
	poisson = lambda l, x: ((l**x) * exp(-l)) / factorial(x)
	n = 1000
	p = 1/216		
	q = 1 - p		
	l = n * p
	X = [poisson(l, x) for x in range(0, 21)]
	plt.stem(X, bins = 18)
	plt.title('Exoerimental Results: Problem 3')
	plt.xlabel('Number of successes in n = 1000 trials')
	plt.ylabel('Probability of success')
	plt.savefig('Poisson.png')

#problem_1(10000)
problem_2()
problem_3()