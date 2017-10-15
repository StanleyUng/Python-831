import numpy as np
import matplotlib.pyplot as plt
from math import factorial, exp

def problem_1(N):
	n = 1000
	# n trials if the sum of 3 rolls is 18, we rolled three 6's
	# X is the # of successes in n trials
	# repeat the experiment N times
	success = [sum([int(sum([np.random.randint(1, 7) for i in range(0, 3)]) == 18) for i in range(0, n)]) for i in range(0, N)]

	b = range(1, 18)
	h1, bin_edges = np.histogram(success, bins = b)
	b1 = bin_edges[0 : 16]
	fig1 = plt.figure(1)
	plt.stem(b1/N, h1)
	plt.title('Probability of rolling three 6\'s')
	plt.xlabel('Number of rolls')
	plt.ylabel('Probability')
	fig1.savefig('Project3Problem1.png')


def problem_2():
	binomial = lambda n, p, q, x : ((factorial(n) // (factorial(x) * factorial(n - x))) * (p**x) * (q**(n - x)))
	n = 1000		# number of trials
	p = 1/216		# probability of success: 3 sixes in a single roll of 3 fair die
	q = 1 - p		# probability of failure

	X = [binomial(n, p, q, x) for x in range(0, 21)]
	print (*X, sep='\n')

	b = range(1, 18)
	h1, bin_edges = np.histogram(X, bins = b)
	b1 = bin_edges[0 : 16]
	fig1 = plt.figure(1)
	plt.stem(b1, h1)
	plt.title('Probability of rolling three 6\'s using Binomial')
	plt.xlabel('Number of rolls')
	plt.ylabel('Probability')
	fig1.savefig('Project3-Problem2.png')


def problem_3():
	poisson = lambda l, x: ((l**x) * exp(-l)) / factorial(x)
	n = 1000
	p = 1/216		
	q = 1 - p		
	l = n * p

	X = [poisson(l, x) for x in range(0, 21)]
	print(*X, sep='\n')
	'''
	b = range(1, 18)
	h1, bin_edges = np.histogram(X, bins = b)
	b1 = bin_edges[0 : 16]
	fig1 = plt.figure(1)
	plt.stem(b1, h1)
	plt.title('Probability of rolling three 6\'s using Poisson')
	plt.xlabel('Number of rolls')
	plt.ylabel('Probability')
	fig1.savefig('Project3-Problem3.png')
	'''
	plt.hist(X, bins = 16)
	plt.show()

'''
#1

Roll 3 fair dice and look at the faces
success is considered if get three 6's
roll it once, what is the prob of success? -> 1/(6^3)
if i do it 1000 times, how many successes would i have?
I want to create the PMF of successes
X = number of successes in 1000 rolls
store those numbers in a list, those numbers will be your histogram

# 2
Binomial

binomial is only success or failure

P(success) = p
P(Fail) = q = 1 - p

Find P(x successed in n trials)

Binomial formula (theoretical calculation)
(n, x) p^x q^(n - x)
'''

#problem_1(10000)
#problem_2()
problem_3()