import numpy as np

def problem_1(N):
    M = [np.random.rand() for i in range(N)]

    P_0 = 0.4
    E_0 = 0.02
    E_1 = 0.03

    success = 0

    for i in range(0, N):
        S = int(not M[i] <= P_0) # create msg S
        R = int(np.random.rand() > E_1) if S == 1 else int(np.random.rand() <= E_0)
        if R != S: # Transmitted incorrectly
            success += 1

    return success / N


def p1_fun(N):
    success += int(not M[i] <= P_0) != int(not np.random.rand() <= E_1) if int(not M[i] <= P_0) else int(np.random.rand() <= E_0)
    return success / N

def problem_2(N):
    E_1 = 0.03
    success = 0
    
    for i in range(0, N):
        R = np.random.rand()
        success += int(R >= E_1)

    return success / N
    
def problem_3(N):
    M = [np.random.rand() for i in range(N)]
    P_0 = 0.4
    E_0 = 0.02
    E_1 = 0.03
    success = 0
    R_success = 0
    
    for i in range(0, len(M)):
        S = int(not M[i] <= P_0) # Create msg S
        R = int(np.random.rand() > E_1) if S == 1 else int(np.random.rand() <= E_0)
        success += int(S == 1 and R == 1)
        R_success += int(R == 1)
    
    return success / R_success
    
def problem_4(N):
    M = [np.random.rand() for i in range(N)]
    P_0 = 0.4
    E_0 = 0.02
    E_1 = 0.03
    success = 0

    for i in range(0, len(M)):
        S = int(not M[i] <= P_0) # Create msg S
        S_bits = [S, S, S] # Transmit the same bit 3 times
        R = list(map(lambda r : int(np.random.rand() > E_1) if S == 1 else int(np.random.rand() <= E_0), S_bits))
        D = int(sum(R) > 0)
        success += int(S != D)

    return success / N

# Print probabilities
print ('Problem 1 p = ' + str(problem_1(100000)))
print ('Problem 2 p = ' + str(problem_2(100000)))
print ('Problem 3 p = ' + str(problem_3(100000)))
print ('Problem 4 p = ' + str(problem_4(100000)))