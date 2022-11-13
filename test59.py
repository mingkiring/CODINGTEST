import sys
input = sys.stdin.readline
N,M =map(int,input().split())
edges = []
distance = [sys.maxsize]*(N+1)

#에지 리스트에 에지 정보 저장
for i in range(M):
    start,end,time = map(int,input().split())
    edges.append((start,end,time))

#벨만 포드 수행
#거리 리스트에 출발 노드 0으로 초기화
distance[1] =0

for _ in range(N-1):
    for start,end,time in edges:
        if distance[start] != sys.maxsize and distance[end]<distance[start]+time:
            distance[end] = distance[start]+time

#음수 사이클 존재하는지 확인
mCycle = False

for start,end,time in edges:
    if distance[start] != sys.maxsize and distance[end] < distance[start]+time:
        mCycle = True

#음수 사이클 미존재 -> 거리 리스트 출력
#음수 사이클 조내 -> -1 출력
if not mCycle:
    for i in range(2,N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)