import sys
import heapq
input = sys.stdin.readline
N,M,K = map(int,input().split())
W = [[] for _ in range(N+1)] # 그래프 정보저장 인접리스트
distance = [[sys.maxsize]*K for _ in range(N+1)] #거리 리스트 K의 row 만큼 만들고 충분히 큰 값을 초기화

for i in range(M):
    a,b,c = map(int,input().split())
    W[a].append((b,c))

#우선순위 큐에 시작노드 저장 #1번 노드 거리 0으로 저장
pq= [(0,1)]
#시작도시 최단 거리 저장 --> 시작적이기때문에 0으로 저장
distance[1][0] = 0

while pq:
    cost, node = heapq.heappop(pq)
    for nNode,nCost in W[node]:
        sCost = cost + nCost #새로운 총 거리 = 현재 노드의 거리 + 에지 가중치
        if distance[nNode][K-1] > sCost:
            distance[nNode][K-1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq,[sCost,nNode])

for i in range(1,N+1):
    if distance[i][K-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][K-1])
