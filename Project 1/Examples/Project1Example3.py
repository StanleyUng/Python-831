import numpy as np
import matplotlib.pyplot as plt

def sum2dice(N):    
    d1 = np.random.randint(1,7,N)   # roll 1
    d2 = np.random.randint(1,7,N)   # roll 2
    s = d1 + d2                     # sum of rolls  
    b = range(1,15)                 # range of numbers  
    h1, bin_edges = np.histogram(s, bins = b)     
    b1 = bin_edges[0:13]     
    # close('all')     
    #    
    fig1 = plt.figure(1)     
    plt.stem(b1,h1)     
    plt.title('Stem plot - Sum of two dice')        # title of graph 
    plt.xlabel('Sum of two dice')                   # x axis label
    plt.ylabel('Number of occurrences')             # y axis label
    fig1.savefig('1 EE381 Proj Stoch Exper-1.png')  # name of file saved  
    #    
    
    fig2 = plt.figure(2)     
    p1 = h1/N     
    plt.stem(b1,p1)     
    plt.title('Stem plot - Sum of two dice: Probability mass function')     
    plt.xlabel('Sum of two dice')     
    plt.ylabel('Probability') 

sum2dice(100)
