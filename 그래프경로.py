# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("그래프경로.txt", "r")

# 
class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def extend(self, data):
        self.stack.extend(data)


def DFS(start, end, nodes, E):
    #global result
    
    # visited 초기화
    # visited = [False] * E
    
    visited = []

    # 스택 초기화 
    st = Stack()

    # stack push
    st.push(start)

    while not st.isEmpty():
        w = st.pop()
    # start 방문
        #visited[start] = True
    #st.push(start)
        # w = st.pop()
        visited.append(w)

        for v in nodes[w]:
            if v not in st.stack + visited:
                st.push(v)
                
    return visited
    
    #return visited

    
    # # 
    # # for i in 

    # do{
    #     neighbors = nodes[start]

    #     for neigh in neighbors:
            


    #     if 

    #     #neighbors = nodes[start] 
    #     w = neighbors[0] 

    #     # 방문안한 w 찾기 인접 정점중
    #     if visited[w] == False:
    #         st.push(start)

    #     while(w){

    #     }


    # }while()

    #print(hi)    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    dic1 = {}

    # Hello py

    #visited = 

    for _ in range(E):
        
        s, e = map(int,input().split())

        if s not in dic1:
            dic1[s] = []
        
        dic1[s].append(e)
    
    start, end = map(int,input().split())

    # print(start)
    # print(end)
    # print(dic1)
    
    print(DFS(start, end, dic1, E))

    

       



        #dic1
        #print(n)

    #print(V)
    #print(E)



    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////