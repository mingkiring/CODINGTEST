import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N,M = map(int,input().split())
parent = [0]*(N+1)

#find 연산 재귀함수
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

#union 연산
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

#checkSame 연산
def checkSame(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else:
        return False

for i in range(0,N+1):
    parent[i] = i

for i in range(M):
    question,a,b = map(int,input().split())
    if question == 0:
        union(a,b)
    else:
        if checkSame(a,b):
            print("Yes")
        else:
            print("No")

