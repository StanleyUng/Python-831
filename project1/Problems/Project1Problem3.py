import numpy as np

N = 100000
success = 0

# deal a sorted hand of 5 cards
def deal():
    # Create a deck from 1 - 52
    deck = np.random.permutation(52) % 13

    # deal a sorted hand
    hand = np.sort(deck[:5])

    # if the 1st and 4th card match OR if the 2nd and 5th card match, it is a 4 of a kind
    # since the hand is in sorted order
    if((hand[0] == hand[3]) or (hand[1] == hand[4])):
        print(hand)

    return ((hand[0] == hand[3]) or (hand[1] == hand[4]))

for i in range(0, N + 1):
    if (deal()):
        success = success + 1

p = success / N
print('The probability of drawing a 4 of a kind is ' + str(p))