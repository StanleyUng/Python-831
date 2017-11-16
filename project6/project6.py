import numpy as np


def problem_1():
	pass

def problem_2():
	pass

N = 10**4	# total number of experiments
n = 15		# number of transitions to be computed


# transition matrix
P = np.matrix( [[1/3, 1/3, 1/3], [1/2, 0, 1/2], [1/4, 1/4, 1/2]] )

D = np.matrix( [1/4, 1/2, 1/4] ) 

plt.title('Simulation results -- States R, N,S');
plt.xlabel('Time step (n)');
plt.ylabel('Prob(State)');
plt.legend('State R', 'State N', 'State S')

for j in range(0, N):
	r0 = np.random.rand()
	if r0 <= D[0, 0]:
		s0 = 'R'
	elif (D[0, 0] + D[0, 1]) >= r0 > D[0, 0]:
		s0 = 'N'
	elif r0 > D[0, 0] + D[0, 2]:
		s0 = 'S'
