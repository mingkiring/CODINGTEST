import sys
from queue import PriorityQueue
input = sys.stdin.readline
N,M = map(int,input().split())
pq = PriorityQueue()
parent = []*(N+1)
##parent 대표 노드 저장 리스트 초기화
for i in range(N+1):
    parent[i] = i
##우선 순위 큐이므로 자동 정렬
for i in range(M):
    s,e,w= map(int,input().split())
    pq.put((w,s,e)) ##제일 앞순서로 정렬되므로 가중치를 제일 먼저 앞에 둬야함

#find 연산
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) #재귀함수
        return parent[a]

#Union 연산
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

#MST 실행
useEdge =0 # 사용 에지 수 저장 변수
result = 0

while useEdge <N-1:
    w,s,e = pq.get()
    if find(s) != find(e):
        union(s,e)
        result += w
        useEdge += 1

print(result)
