import numpy as np

# A single experiment: 100 tosses a coin
def toss():
    # returns 0 or 1
    # 0 for tails, 1 for heads
    return np.random.randint(0, 2, 100)

# # of times we want to repeat the experiment
N = 100000

# # of successful experiments
success = 0.0

# Perform the experiment N times
for i in range(0, N + 1):
    if (sum(toss()) == 50):
        success = success + 1

# The probability is # of successful experiments / Total # of experiments
p = success / N
print('The probability of getting exactly 50 heads in 100 tosses of a coin is ' + str(p))