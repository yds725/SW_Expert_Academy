#
#
from pprint import pprint

numList = [True] * (123456*2)
for i in range(2, int((123456*2)**0.5)+2):
    if numList[i] == True:
        for j in range(2*i, 123456*2 + 1, i):
            if j >= len(numList):
                break

            numList[j] = False
primeList = [i for i in range(2, 123456*2) if numList[i] == True]

pprint(primeList)
