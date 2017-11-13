'''
create a popultion of bearings
N = 1000000
choose a sample of n randn for std normal


calculate the sample mean, 

z = (x - mu) / sigma

mu = 75
sigma = 0.75


B = random.sample(N), n
random numbers out of B

X = B()

pop -> mean of sample -> plot it





'''

import numpy as np 
import matplotlib as plt


'''
expectation(x_hat) == mu_x_hat == mu
expectation[(x_hat - mu_x_hat)**2] == sigma_x_hat**2 == (sigma**2 / n) 
 

'''




def problem_1():
	N = 10**6		# Total number of bearings
	mu = 75			# sample mean 
	sigma = 0.75	# standard deviation
	n = range(1, 201)	# sample size n 1 - 200

	# generate population
	B = mu + np.random.sample(N) * sigma

	






















