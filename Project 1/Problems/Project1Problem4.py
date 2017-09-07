import numpy as np
import string

def generatePassword():
    password = ''
    for i in range(0, 4):
        password += string.ascii_letters[np.random.randint(0, 26)]
    return password

def generateList():
    N = 10**5
    passwords = []
    for i in range (0, N):
        passwords.append(generatePassword())
    return passwords

N = 10
yourPassword = generatePassword()
success = 0

for i in range(0, N):
    hackerlist = generateList()
    if (yourPassword in hackerlist):
        success = success + 1
    
p = success / N
print('The probability of a hacker having your password is ' + str(p))