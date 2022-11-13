import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
distance = [[sys.maxsize for j in range(N+1)]for i in range(N+1)] #충분히 큰 값으로 초기화

for i in range(1,N+1):
    distance[i][i] =0 #인접 행렬에 시작도시와 종료 도시가 같은 자리에 0 저장

for i in range(M):
    s,e,v= map(int,input().split())
    if distance[s][e]>v:
        distance[s][e] =v #노선 데이터를 distance 행렬에 저장

####가장 중요한 부분#####
for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] +distance[k][j]

#정답 리스트 출력
for i in range(1,N+1):
    for j in range(1,N+1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[i][j],end=' ')
    print()