import enchant
from itertools import permutations

def main():

    letters = raw_input("Input the letters in your rack:\n")
    options = list([''.join(i) for i in permutations(letters, 2)])
    for p in xrange(3, len(letters)):
        options.extend(list([''.join(j) for j in permutations(letters, p)]))

    for data in options:
        if isword(data):
            print data + " ", playscrabble(data)

def isword(x):
    d = enchant.Dict("en_US")
    return d.check(x)


def playscrabble(x):

    length = len(x)
    count = 0

    for y in xrange(0, length, 1):
        if (x[y] == 'a') or (x[y] == 'e') or (x[y] == 'i') or (x[y] == 'l') or (x[y] == 'n') or (x[y] == 'o') or (x[y] == 'r') or (x[y] == 's') or (x[y] == 't') or (x[y] == 'u'):
            count += 1
        elif (x[y] == 'd') or (x[y] == 'g'):
            count += 2
        elif (x[y] == 'b') or (x[y] == 'c') or (x[y] == 'm') or (x[y] == 'p'):
            count += 3
        elif (x[y] == 'f') or (x[y] == 'h') or (x[y] == 'v') or (x[y] == 'w') or (x[y] == 'y'):
            count += 4
        elif x[y] == 'k':
            count += 5
        elif (x[y] == 'j') or (x[y] == 'x'):
            count += 8
        elif (x[y] == 'q') or (x[y] == 'z'):
            count += 10

    return count
