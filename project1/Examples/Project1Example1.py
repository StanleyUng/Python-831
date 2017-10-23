import numpy as np

def coin(N):        
    heads, tails = 0, 0     
    for k in range(0,N):         
        coin = np.random.randint(0,2)         
        if coin == 1:             
            heads = heads + 1         
        else:             
            tails = tails + 1     
    #    
    p_heads=heads/N     
    p_tails=tails/N     
    print('probability of heads = ', p_heads)     
    print('probability of tails = ', p_tails) 

# call
coin(100000)