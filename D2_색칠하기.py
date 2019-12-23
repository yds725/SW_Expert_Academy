#def

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
sys.stdin = open("색칠하기.txt", "r")

def draw_color(N, dic):

    # 2d-array 10x10
    panel = [[0] * 10 for _ in range(10)]

    for i in range(N):
        arr = dic[i]

        r1 = arr[0]
        c1 = arr[1]

        r2 = arr[2]
        c2 = arr[3]

        color = arr[4]
        # 숫자 1 또는 2 를 넣어서 마치 색 칠하듯 시발 
        for i in  (r1, r2 + 1):
            for j in (c1, c2 + 1):
                
                if panel[i][j] == 0 or panel[i][j] == color:
                    panel[i][j] = color
                else:
                    panel[i][j] = panel[i][j] + color




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    dic = {}

    for i in range(N):
        arr = list(map(int, input().split()))
    
        dic[i] = arr


    print(dic) 

        

    

    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
