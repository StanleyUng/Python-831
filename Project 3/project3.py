import numpy as np
import random
import matplotlib.pyplot as plt

def problem_1(N):
	n = 1000
	# n trials if the sum of 3 rolls is 18, wee rolled three 6's
	# X is the # of successes in n trials
	# repeat the experiment N times
	success = [sum([int(sum([np.random.randint(1, 7) for i in range(0, 3)]) == 18) for i in range(0, n)]) for i in range(0, N)]

	b = range(1, 18)
	h1, bin_edges = np.histogram(success, bins = b)
	b1 = bin_edges[0 : 16]
	fig1 = plt.figure(1)
	plt.stem(b1/N, h1)
	plt.title('Stem plot - Sum of two dice')
	plt.xlabel('Number of rolls')
	plt.ylabel('Number of occurrences')
	fig1.savefig('2 EE381 Proj Stoch Exper-1.png')

def problem_2(N):
	n = 1000
	p = (1/6)
	q = (1 - p)
	x = 3
	# (1000, 3)

	(p**x) * (q**(n - x))



#def problem_3(N):

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

problem_1(10000)