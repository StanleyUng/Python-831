import numpy as np
import string

possiblePasswords = 26**4

# The number way
def generatePassword():
    return np.random.randint(0, possiblePasswords)

def generateList(x):
    return np.random.randint(0, possiblePasswords, x)

# # of trials
N = 1000
yourPassword = generatePassword()
success = 0

hackerListSize = 317000

for i in range(0, N):
    hackerlist = generateList(hackerListSize)
    if (yourPassword in hackerlist):
        success = success + 1
    
p = success / N
print('The probability of a hacker having your password is ' + str(p))