
import numpy as np 
import matplotlib.pyplot as plt

def problem_1():
	Nb = 10**6		# Total number of bearings
	mu = 75			# sample mean 
	sigma = 7.5		# standard deviation
	n = range(1, 201) # range from 1 to 200

	plt.title('Sample Means and 95% Confidence Intervals')
	plt.xlabel('Sample Size n')
	plt.ylabel('x_bar')

	B = mu + np.random.standard_normal(Nb) * sigma
	x_bar = [np.mean(np.random.choice(B, i)) for i in n]

	# Sample Means (n, x_bar)
	plt.plot(n, list(x_bar), 'x', n, np.repeat(mu, len(n)), 'k')

	# 95% Confidence Interval
	plt.plot(n, mu + 1.96 * sigma/np.sqrt(n), 'r--', n, mu - 1.96 * sigma/np.sqrt(n), 'r--')

	# 99% Confidence Interval
	plt.plot(n, mu + 2.58 * sigma/np.sqrt(n), 'g:', n, mu - 2.58 * sigma/np.sqrt(n), 'g:')

	plt.show()

N = 1000000
mu = 75 
sigma = 7.5 
n = range(1, 201)
bearings = mu + np.random.standard_normal(N) * sigma 

# j: sample size
def problem_2(j):
	Nb = 10**6		# Total number of bearings
	mu = 75			# sample mean 
	sigma = 7.5		# standard deviation
	B = mu + np.random.standard_normal(Nb) * sigma # random sample
	M = 10**5 		# number of trials

	'''
	5:		2.78, 4.6
	40:		2.02, 2.70
	120:	1.98, 2.62
	'''

	# number of successes for each method
	success_95_n = 0
	success_99_n = 0
	success_95_t = 0
	success_99_t = 0

	# run M trials
	for i in range(0 , M):
		# create a random sample
		x_j = np.random.choice(B, j)
		x_bar = np.mean(x_j)
		s_hat = np.sqrt(sum((x_j - x_bar)**2) / (j - 1))

		# 95% Confidence Normal
		n_95_lower = x_bar - 1.96 * (s_hat / np.sqrt(j))  
		n_95_upper = x_bar + 1.96 * (s_hat / np.sqrt(j))

		if n_95_lower <= mu <= n_95_upper:
			success_95_n += 1

		# 99% Confidence Normal
		n_99_lower = x_bar - 2.58 * (s_hat / np.sqrt(j))  
		n_99_upper = x_bar + 2.58 * (s_hat / np.sqrt(j))

		if n_99_lower <= mu <= n_99_upper:
			success_99_n += 1

		# 95% Confidence t Distribution
		t_95_lower = x_bar - 2.78 * (s_hat / np.sqrt(j))
		t_95_upper = x_bar + 2.78 * (s_hat / np.sqrt(j))

		if t_95_lower <= mu <= t_95_upper:
			success_95_t += 1

		# 99% Confidence t Distribution
		t_99_lower = x_bar - 4.6 * (s_hat / np.sqrt(j))
		t_99_upper = x_bar + 4.6 * (s_hat / np.sqrt(j))

		if t_99_lower <= mu <= t_99_upper:
			success_99_t += 1

	success = [success_95_n, success_99_n, success_95_t, success_99_t]
	print ([s / M for s in success])



#problem_1()
problem_2(5)