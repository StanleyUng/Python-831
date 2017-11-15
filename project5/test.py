import numpy as np
import matplotlib.pyplot as plt

Nb = 10**6		# Total number of bearings
mu = 75			# sample mean 
sigma = 7.5		# standard deviation
B = mu + np.random.standard_normal(Nb) * sigma # random sample

M = 10**5 # number of trials

# Used to store into a table format
success = {5: [0,0,0,0], 40: [0,0,0,0], 120: [0,0,0,0]}
t_crit = {5: [2.78, 4.6], 40: [2.02, 2.70], 120: [1.98, 2.62]}
values = success.keys()

j = 5

success_95_n = 0
success_99_n = 0
success_95_t = 0
success_99_t = 0

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
success = [s / M for s in success]

print (success)