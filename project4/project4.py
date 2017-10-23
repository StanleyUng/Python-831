'''
uniform(a, b, n)
a - b range from a to b
generate n numbers
'''

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def problem_1(n):
	N = 10000

	mu, sigma = 100, 15
	x = [sum(np.random.uniform(1, 3, 2)) for i in range(0, N)]

	# the histogram of the data
	n, bins, patches = plt.hist(x, bins = 20, normed=1, facecolor='yellow', alpha=0.75)
	# add a 'best fit' line
	y = mlab.normpdf(bins, mu, sigma)
	l = plt.plot(bins, y, 'r--', linewidth=1)
	plt.xlabel('Book stack height for n = 2 books')
	plt.ylabel('PDF')
	plt.title('PDF of book stack height and comparison with Gaussian')
	plt.axis([0, 8, 0, 0.30])
	plt.grid(True)
	plt.show()

problem_1(10000)