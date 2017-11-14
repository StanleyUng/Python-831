
import numpy as np 
import matplotlib.pyplot as plt

def problem_1():
	Nb = 10**6		# Total number of bearings
	mu = 75			# sample mean 
	sigma = 7.5	# standard deviation
	n = range(1, 201) # range from 1 to 200

	plt.title('Sample Means and 95% Confidence Intervals')
	plt.xlabel('x_bar')
	plt.ylabel('Sample Size n')

	B = list(mu + np.random.sample(Nb) * sigma)

	# this shit works
	x_bar = [np.mean(B[int(np.ceil(np.random.rand() * Nb))]) for i in n]
	#x_bar = [np.mean(np.random.choice(B, i)) for i in n]
	#x_bar = [np.mean(B[:i]) for i in n]

	# Sample Means (n, x_bar)
	plt.plot(n, x_bar, 'x', n, np.repeat(mu, len(n)), 'k')

	# 95% Confidence Interval
	plt.plot(n, mu + 1.96 * sigma/np.sqrt(n), 'r--', n, mu - 1.96 * sigma/np.sqrt(n), 'r--')

	# 99% Confidence Interval
	plt.plot(n, mu + 2.58 * sigma/np.sqrt(n), 'g:', n, mu - 2.58 * sigma/np.sqrt(n), 'g:')

	plt.show()


def  problem_2():
	pass


problem_1()



















