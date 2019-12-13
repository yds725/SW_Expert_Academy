# brr = [[1,2,3]] * 3
# print(brr)

# n, m = map(int, input().split())

# mylist = [0 for _ in range(n)]

# for i in range(n):
#     mylist[i] = list(map(int,input().split()))

# print(mylist)

n, m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(n)]

# column wise travel
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j]

for j in range(len(arr[0])):
    for i in range(len(arr)):
        arr[i][j]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j + (m-1-2*j)*(i%2)]


