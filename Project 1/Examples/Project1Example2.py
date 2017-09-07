import numpy as np

def coin2(N):       
    coin = np.random.randint(0,2,N)
    heads = sum(coin)     
    tails = N - heads     
    #    
    p_heads = heads/N     
    p_tails = tails/N     
    print('probability of heads = ', p_heads)  
    print('probability of tails = ', p_tails) 

coin2(10000)