#줄 세우기
from collections import deque
N, M = map(int,input().split())
A = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

#인접리스트 저장 M만큼 반복
for i in range(M):
    S,E = map(int,input().split())
    A[S].append(E)
    indegree[E] += 1

#위상정렬 수행
queue = deque()

#진입 차수 리스트 0이면 큐에 삽입
for i in range(1,N+1):
    if indegree[i] ==0:
        queue.append(i)

#큐가 빌떄까지 위상정렬 수행
while queue:
    now = queue.popleft()
    print(now,end=' ')
    for next in A[now]:
        indegree[next] -= 1
        if indegree[next] ==0:
            queue.append(next)
