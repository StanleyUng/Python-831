import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def problem_1():
	N = 10000
	a = 1; b = 3 # a=min bookwidth ; b=max bookwidth
	nbooks = 15 # Number of books
	nbins = 30 # Number of bins
	mu= 2; sigma = 0.33; sig_sqrt = 0.57

	X = [sum(np.random.uniform(a, b, nbooks)) for i in range(0, N)]
	
	# Create bins and histogram
	bins = [float(x) for x in np.linspace(nbooks * a, nbooks * b,nbins + 1)]
	h1, bin_edges = np.histogram(X, bins, density=True)
	# Define points on the horizontal axis
	be1 = bin_edges[0 : len(bin_edges) - 1]
	be2 = bin_edges[1 : len(bin_edges)]
	b1 = (be1 + be2) / 2
	barwidth = b1[1] - b1[0] # Width of bars in the bargraph
	plt.close('all')
	plt.bar(b1, h1, width = barwidth, edgecolor = 'w')
	fig1 = plt.figure(1)
	plt.plot(b1, 1 / ((sig_sqrt*np.sqrt(nbooks)) * np.sqrt(2 * np.pi)) * np.exp(-(b1 - (mu * nbooks))**2 / (2 * (sig_sqrt * np.sqrt(nbooks)))), color = 'r')

	# Labels
	plt.xlabel('Book stack height for n = ' + str(nbooks) + ' books')
	plt.ylabel('PDF')
	plt.title('PDF of book stack height and comparison with Gaussian')
	plt.show()

def problem_2():
	N = 10000
	beta = 0.5
	nbins = 30
	edgecolor = 'w'
	mu, sigma, sig_sqrt = 2, 0.33, 0.57

	X = np.random.exponential(beta, N)

	# Create bins and histogram
	bins = np.linspace(0, 5)
	h1, bin_edges = np.histogram(X, bins, density=True)
	# Define points on the horizontal axis
	be1 = bin_edges[0 : len(bin_edges) - 1]
	be2 = bin_edges[1 : len(bin_edges)]
	b1 = (be1 + be2) / 2
	barwidth = b1[1] - b1[0] # Width of bars in the bargraph
	plt.close('all')
	plt.bar(b1, h1, width = barwidth, edgecolor = 'w')
	plt.plot(bins, 2 * np.exp(-2 * bins), color='r')

	fig1 = plt.figure(1)

	# Labels
	plt.xlabel('Random Variable T')
	plt.ylabel('PDF')
	plt.title('Exponentially Distributed RV')
	plt.show()

def problem_3():
	N = 10000
	beta = 45
	carton_vector = 24
	nbins = 30

	X = [sum(np.random.exponential(beta, carton_vector)) for i in range(0, N)]
	
	# Create bins and histogram
	bins = [float(x) for x in np.linspace(carton_vector, 2500, nbins + 1)]
	h1, bin_edges = np.histogram(X, bins, density = True)
	# Define points on the horizontal axis
	be1 = bin_edges[0 : len(bin_edges) - 1]
	be2 = bin_edges[1 : len(bin_edges)]
	b1 = (be1 + be2) / 2
	barwidth = b1[1] - b1[0] # Width of bars in the bargraph
	plt.close('all')
	plt.bar(b1, np.cumsum(h1) * barwidth, width = barwidth, edgecolor = 'w')
	
	# Plots the red line on the same graph as the bar graph
	plt.axhline(y = 1.0, color='r')

	fig1 = plt.figure(1)
	# Labels
	plt.xlabel('Lifetime of battery T')
	plt.ylabel('PDF of battery life')
	plt.title('Distribution of Sum of RV: Battery Life')
	plt.show()

#problem_1()
#problem_2()
problem_3()