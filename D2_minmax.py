import sys 
import functools as ft
#cn = input() 
#a = [sys.stdin.readline() for i in range(n)]
#a = list(map(int, sys.stdin.readline().split()))

f = sys.stdin
flag = True

while flag:
    line = f.readline()
    print(line.split())

    lst1 = line.split()
    a = ft.reduce((lambda x,y = x+y), lst1)
    reduce
    print(a)
    #print(line.split()[0])
    #print(line.split()[1])
    #print(line)
    if line == '':
        flag = False


#print(a)

