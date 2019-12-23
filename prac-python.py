# brr = [[1,2,3], [4,5,6]] 

# print(brr[0])


# print(brr)

# brr = [[1,2,3] for i in range(3)]

# n, m = map(int, input().split())

# mylist = [0 for _ in range(n)]

# for i in range(n):
#     mylist[i] = list(map(int,input().split()))

# print(mylist)

# n, m = map(int, input().split())
# mylist = [list(map(int, input().split())) for _ in range(n)]

# column wise travel
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         arr[i][j]

# # row wise travel
# for j in range(len(arr[0])):
#     for i in range(len(arr)):
#         arr[i][j]

# 지그재그 여행
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         arr[i][j + (m-1-2*j)*(i%2)]

# 전치 행렬 (행과 열 값이 반대인 의미)
# 
#  
# zip(*matrix)
# arr = [[1,2,3], [4,5,6], [7,8,9]]

# for i in range(3):
#     for j in range(3):
#         if i < j:
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# 비트 리스트 부분집합
# 16진수 비트? 
# 1 << n -> n: 부분 집합의 개수 
# i & (1 << j)

arr = [3,6,7,1,5,4]

n = len(arr) # n 

for i in range(1<<n): # 1 << n subset numbers
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=",")
    print()

### binary search
# 자료 중앙에 있는 원소 선택
# 중앙 원소 값 찾고자 하는 목표 값 비교
# 목표 값 < 중앙 원소 값 : 자료 왼쪽 반 새로 검색 수행 
# 검색 범위 시작점 종료점 이용하여 검색을 반복 수행
# 이진 검색 자료에 삽입과 삭제가 발생 리스트 상태를 항상 정렬 상태로 유지하는 추가 작업 필요

def binarySearch(a, key):
    start = 0
    end = len(a) - 1

    while start <= end:
        middle = start + (end - start) // 2
        if key  == a[middle]:
            return # True 검색 성공
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
    
    return False # 검색 실패

### selection sorting
# 주어진 자료들 가장 작은 값 원소부터 차례대로 선택 위치를 교환 방식
# 셀렉션 알고맂ㅁ 전체 자료에 적용 

def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i

        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]



