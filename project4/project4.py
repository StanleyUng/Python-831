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
	#x = [1, 5, 10, 15]

	x = [sum(np.random.uniform(1, 3, 1)) for i in range(0, N)]

	# the histogram of the data
	n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

	plt.xlabel('Smarts')
	plt.ylabel('Probability')
	plt.title('Histogram of book thiccness')
	plt.axis([40, 160, 0, 3])
	plt.grid(True)
	plt.show()

problem_1(10000)