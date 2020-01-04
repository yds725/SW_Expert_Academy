# 스택
# 선형구조
# 마지막에 삽입한 자료를 가장 먼저 꺼냄

# 후입선출: LIFO (Last In First Out
#
# stack implementation 
#  push , pop, peek
# top -> 마지막 삽입된 원소의 위치 스택에서 

# 파이썬 어펜드 팝은 스택 이다
# 리스트를 사용하여 스택 구현 하는 경우

# 단점: 리스트의 크기를 변경하는 작업은 내부적으로 큰 오버헤드 발생 작업으로 많은 시간이 소요
# 대책: 동적 연결리스트 이용하여 저장소 동적으로 할당 스택 구현 방법


# 함수 호출 프로그램 , 복귀에 따른 수행 순서를 관리
# 가장 마지막에 호출된 함수가 먼저 실행 완료 복귀하는 후입선출 구조 스택 이용하여 수행순서 관리

# 자기 자신 호출하여 순환 수행:?

def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)


### Memoization 
# 동적계획법 핵심이 되는 기술 
## DP(동적 계획법)
# 리커시브 피보1 : 재귀적 구조 시스템 호출 스택 을 사용하는 오버헤드
# 이터레이티브 피보2: 메모이제션 

### DFS
# 깊이 우선탐색 뎁스퍼스트서치
# 후출입 스택 사용 

visited[] stack[]
DFS(v)
    v 방문;
    visited[v] <- True
    do{
        if (v 인접 정점 중 방문 안 한 w 찾기)
            push(v)
        while(w) {
            w 방문
            visited[w] <- True
            push(w)
            v <- w
            v 인접 정점 중 방문 안 한 w찾
        }
        v <- pop(stack)
    } while(v)

end DFS()

### BFS
# 너비 우선 탐색 



