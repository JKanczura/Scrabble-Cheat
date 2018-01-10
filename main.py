import enchant
from itertools import permutations

def main():

    letters = raw_input("Input the letters in your rack:\n")
    options = list( [''.join(i) for i in permutations(letters)])
    words = list()
    for data in options:
        if (isWord(data) == True):
            words.append(data)
    print words



def isWord(x):
    d = enchant.Dict("en_US")
    return d.check(x)

def playScrabble(x):
    '''
    A = 1
    B = 3
    C = 3
    D = 2
    E = 1
    F = 4
    G = 2
    H = 4
    I = 1
    J = 8
    K = 5
    L = 1
    M = 3
    N = 1
    O = 1
    P = 3
    Q = 10
    R = 1
    S = 1
    T = 1
    U = 1
    V = 4
    W = 4
    X = 8
    Y = 4
    Z = 10
    '''
