'''
uniform(a, b, n)
a - b range from a to b
generate n numbers
'''

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def problem_1(nbooks):
	a = 1; b = 3 # a=min bookwidth ; b=max bookwidth
	#nbooks = 5 # Number of books
	nbins = 30 # Number of bins
	edgecolor = 'w' # Color separating bars in the bargraph
	N = 10000

	# X is the array with the values of the RV to be plotted
	X = [sum(np.random.uniform(a, b, nbooks)) for i in range(0, N)]
	
	# Create bins and histogram
	bins = [float(x) for x in np.linspace(nbooks * a, nbooks * b,nbins + 1)]
	h1, bin_edges = np.histogram(X, bins, density=True)
	# Define points on the horizontal axis
	be1 = bin_edges[0 : len(bin_edges) - 1]
	be2 = bin_edges[1 : len(bin_edges)]
	b1 = (be1 + be2) / 2
	barwidth = b1[1] - b1[0] # Width of bars in the bargraph

	fig1 = plt.figure(1)

	# Labels
	plt.xlabel('Book stack height for n = ' + str(nbooks) + ' books')
	plt.ylabel('PDF')
	plt.title('PDF of book stack height and comparison with Gaussian')
	plt.bar(b1, h1, width = barwidth, edgecolor = edgecolor)
	plt.show()

def problem_2():
	N = 10000
	beta = 0.5

	nbins = 30 # Number of bins
	edgecolor = 'w' # Color separating bars in the bargraph

	X = np.random.exponential(beta, N)

	plt.hist(X, bins = 30)
	plt.xlabel('')
	plt.ylabel('')
	plt.title('')
	plt.bar(1, 10, width = 1, edgecolor = edgecolor)
	plt.show()

def problem_3():
	a = 1; b = 3 # a=min bookwidth ; b=max bookwidth
	#nbooks = 5 # Number of books
	nbins = 30 # Number of bins
	edgecolor = 'w' # Color separating bars in the bargraph
	N = 10000
	beta = 45

	X = np.random.exponential(beta, N)
	
	# Create bins and histogram
	bins = [float(x) for x in np.linspace(24 * a, 24 * b,nbins + 1)]
	h1, bin_edges = np.histogram(X, bins, density=True)
	# Define points on the horizontal axis
	be1 = bin_edges[0 : len(bin_edges) - 1]
	be2 = bin_edges[1 : len(bin_edges)]
	b1 = (be1 + be2) / 2
	barwidth = b1[1] - b1[0] # Width of bars in the bargraph
	fig1 = plt.figure(1)
	# Labels
	plt.xlabel('Book stack height for n = ' + str(nbooks) + ' books')
	plt.ylabel('PDF')
	plt.title('PDF of book stack height and comparison with Gaussian')
	plt.bar(b1, h1, width = barwidth, edgecolor = edgecolor)
	plt.show()

'''
#3 is literally #1
24 of soemthing, #1 books are uniform,
#3 is not uniform, so use exponential distribution
replace 15 books with 24
instead of adding 15, now add 24
'''


#problem_1(1)
problem_2()
#problem_3()