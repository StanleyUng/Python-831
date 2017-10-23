import numpy as np
import matplotlib.pyplot as plt

# Number of experiments
N = 100000

def roll(N):
    num = []
    for i in range(0, N + 1):
        sum = 0
        count = 0
        while(sum != 7):
            sum = np.random.randint(1, 7) + np.random.randint(1, 7)
            count = count + 1
        num.append(count)

    b = range(1, 30)                 # range of numbers  
    h1, bin_edges = np.histogram(num, bins = b)     
    b1 = bin_edges[0 : 28]
    # close('all')
    fig1 = plt.figure(1)                            # declare figure
    plt.stem(b1,h1)                                 # type of plot, stem plot
    plt.title('Stem plot - Sum of two dice')        # title of graph 
    plt.xlabel('Number of rolls')                   # x axis label
    plt.ylabel('Number of occurrences')             # y axis label
    fig1.savefig('2 EE381 Proj Stoch Exper-1.png')  # name of file saved  

roll(N)